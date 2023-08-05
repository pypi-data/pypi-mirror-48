

from lmf.dbv2 import db_command ,db_query
from lmf.bigdata import pg2csv
import sys 
import os 
from fabric import Connection

import traceback
def est_t_gg(conp):
    sql="""
    create table v3.t_gg (
    html_key  serial,
    guid text ,
    gg_name text not null ,
    href text  not null ,

    fabu_time timestamp(0),

    ggtype text not null ,
    jytype text not null ,
    diqu text,
    quyu text not null,
    info text,
    page text ,
    create_time timestamp(0))
    partition by list(quyu)
    (partition anhui_anqing values('anhui_anqing'),
    partition anhui_bengbu values('anhui_bengbu')
    )

    """

#为 gg表新增\删除分区
def add_partition_t_gg(quyu,conp):
    user,password,ip,db,schema=conp
    sql="alter table %s.t_gg add partition %s values('%s')"%(schema,quyu,quyu)
    db_command(sql,dbtype='postgresql',conp=conp)

def drop_partition_t_gg(quyu,conp):
    user,password,ip,db,schema=conp
    sql="alter table %s.t_gg drop partition for('%s')"%(schema,quyu)
    db_command(sql,dbtype='postgresql',conp=conp)


def est_cdc_t_gg(quyu,addr,conp):
    #quyu="anhui_bozhou"
    arr=quyu.split("_")
    s1,s2=arr[0],'_'.join(arr[1:])
    #addr="192.168.4.187:8111"
    #conp=['gpadmin','since2015','192.168.4.179','base_db','cdc']
    sql="""create  external table cdc.t_gg_cdc_%s (guid text,gg_name text ,fabu_time timestamp,gg_href  text  ,ggtype text,jytype text
     , diqu text,quyu text  ,info text,page text ) 
    location('gpfdist://%s/t_gg_cdc_%s.csv') format 'csv' (delimiter '\001' header quote '\002') log errors into errs segment reject limit 1000;  
    """%(quyu,addr,quyu)

    db_command(sql,dbtype="postgresql",conp=conp)





#将pg数据导入到文件系统下的csv

def out_t_gg_all(quyu,dir,conp):
    path1=os.path.join(dir,"t_gg_cdc_%s.csv"%quyu)
    print(path1)
    arr=quyu.split("_")
    s1,s2=arr[0],'_'.join(arr[1:])
    sql="""select distinct on(gg_name,href,quyu) encode(digest(name||a.href||'anhui_anqing','md5'),'hex') as guid ,
        name as gg_name,ggstart_time::timestamp(0) as fabu_time,a.href,ggtype,jytype,diqu,'%s' as quyu,info
        ,replace(replace(replace(replace(b.page,'\001',''),'\002',''),'\r',''),'\n','') as page
        from %s.gg as a ,%s.gg_html  as b where a.href=b.href
        """%(quyu,s2,s2)
    print(sql)
    #df=db_query(sql=sql,dbtype="postgresql",conp=conp)

    #df.to_csv(path1,sep='\001',quotechar='\002',index=False)
    pg2csv(sql,conp,path1,chunksize=10000,sep='\001',quotechar='\002')



def out_t_gg_cdc(quyu,dir,conp):
    #quyu="anhui_chizhou"
    path1=os.path.join(dir,"t_gg_cdc_%s.csv"%quyu)
    arr=quyu.split("_")
    s1,s2=arr[0],'_'.join(arr[1:])
    sql1="select table_name  from information_schema.tables where table_schema='%s' and table_name ~'.*gg_cdc$'"%(s2)
    df1=db_query(sql=sql1,dbtype="postgresql",conp=conp)

    sqls=["""select name,href,ggstart_time from %s.%s """%(s2,w) for w in df1['table_name']]
    sql=" union all ".join(sqls)

    sql="""with b as(%s)
        , b1 as (
       select name ,href,ggstart_time,ggtype,jytype,diqu,info from %s.gg as a where  exists(select 1 from b where a.name=b.name and 
       a.href=b.href and a.ggstart_time=b.ggstart_time and b.name is not null and b.href is not null and b.ggstart_time is not null ) )

        select distinct on(gg_name,href,quyu) encode(digest(name||b1.href||'anhui_anqing','md5'),'hex') as guid ,
        name as gg_name,ggstart_time::timestamp(0) as fabu_time,b1.href,ggtype,jytype,diqu,'%s' as quyu,info
        ,replace(replace(replace(replace(b.page,'\001',''),'\002',''),'\r',''),'\n','') as page
        from b1 ,%s.gg_html  as b where b1.href=b.href 
     """%(sql,s2,quyu,s2)
    print(sql)
    #df=db_query(sql=sql,dbtype="postgresql",conp=conp)
    #df.to_csv(path1,sep='\001',quotechar='\002',index=False)
    pg2csv(sql,conp,path1,chunksize=10000,sep='\001',quotechar='\002')


def update_t_gg(quyu,conp):

    user,password,ip,db,schema=conp

    sql="""
    insert into %s.t_gg(guid,gg_name,fabu_time,href,ggtype,jytype,diqu,quyu,info,create_time,page)
    SELECT 
    distinct on(guid)
    guid,gg_name,fabu_time,gg_href,ggtype,jytype,diqu,quyu,info,now()::timestamp(0) as create_time,page

     FROM cdc.t_gg_cdc_%s a where not exists (select 1 from %s.t_gg as b where quyu='%s' and a.guid=b.guid)  and gg_name is not null
    
    """%(schema,quyu,schema,quyu)

    db_command(sql,dbtype='postgresql',conp=conp)



def add_quyu_tmp(quyu,conp_pg,conp_hawq,dir,addr,tag='all'):
    print("t_gg表更新")
    user,password,ip,db,schema=conp_hawq
    print("1、准备创建分区")
    sql="""
    SELECT  partitionname
    FROM pg_partitions
    WHERE tablename='t_gg' and schemaname='%s'
    """%(schema)
    df=db_query(sql,dbtype="postgresql",conp=conp_hawq)
    if quyu in df["partitionname"].values:
        print("%s-partition已经存在"%quyu)

    else:
        print('%s-partition还不存在'%quyu)
        add_partition_t_gg(quyu,conp_hawq)

    print("2、准备创建外部表")

    sql="""
    select tablename from pg_tables where schemaname='cdc'
    """
    df=db_query(sql,dbtype="postgresql",conp=conp_hawq)
    ex_tb='t_gg_cdc_%s'%quyu
    if ex_tb in df["tablename"].values:
        print("外部表%s已经存在"%quyu)

    else:
        print('外部表%s还不存在'%quyu)
        est_cdc_t_gg(quyu,addr,conp_hawq)

    print("3、准备从RDBMS导出csv")
    if tag=='all':
        out_t_gg_all(quyu,dir,conp_pg)
    else:
        out_t_gg_cdc(quyu,dir,conp_pg)

    print("4、hawq中执行更新、插入语句")

    update_t_gg(quyu,conp_hawq)

def add_quyu(quyu,tag='all'):

    conp_pg=["postgres","since2015","192.168.4.175","anhui","bengbu"]
    conp_hawq=["gpadmin","since2015","192.168.4.179","base_db","v3"]
    dir='/data/lmf'
    addr='192.168.4.187:8111'
    add_quyu_tmp(quyu,conp_pg,conp_hawq,dir,addr,tag=tag)









