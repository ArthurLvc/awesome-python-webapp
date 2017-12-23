import time,uuid
#coding:utf-8

from transwarp.db import next_id
from transwarp.orm import Model,StringField,BooleanField,FloatField,TextField

class User(Model):
	__table__ = 'users'
	
	id = SringField(primary_key = True,default = next_id,ddl = 'varchar(50)')
	email = StringField(updatable = False,ddl = 'varchar(50)')
	password = StringField(ddl = 'varchar(50)')
	admin = BooleanField()
	name = StringField(ddl = 'varchar(50)')
	image = StringField(ddl = 'varchar(500)')
	created_at = FloatField(updatable = False,default = time.time)

class Blog(Model):
	__table__ = 'blogs'
	
	id = StringField(primary_key = True,default = next_id,ddl = 'varchar(50)')
	user_id = StringField(updatable = False,ddl = 'varchar(50)')
	user_name = StringField(ddl = 'varchar(50)')
	user_image = StringField(ddl = 'varchar(500)')
	name = SringField(ddl = 'varchar(50)')
	summary = StringField(ddl = 'varchar(200)')
	content = TextField()
	created_at = FloatField(updatable = False,default = time.time)

class  Comment(Model):
	__table__ = 'comments'
	
	id = StringField(primary_key = True,default = next_id,ddl = 'varchar(50)')
	blog_id = SringField(updatable = False,ddl = 'varchar(50)')
	user_id = SringField(updatable = False,ddl = 'varchar(50)')
	user_name = StringField(ddl = 'varchar(50)')
	user_image = StringField(ddl = 'varchar(500)')
	content = TextField()
	created_at = FloatField(updatable = False,default = time.time)
	
-- schema.sql

drop database if exists awesome;

create database awesome;

use awesome;

grant select,insert,update,delete on awesome.* to 'www-data'@'localhost' identified by 'www-data';

create table users(
	'id' varchar(50) not null,
	'email' varchar(50) not null,
	'password' varchar(50) not null,
	'admin' bool not null,
	'name' varchar(50) not null,
	'image' varchar(500) not null,
	'created_at' real not null,
	unique key 'idx_email' ('created_at'),
	key 'idx_created_at'('created_at),
	primary_key ('id')
) engine = innodb default charset = utf-8;

create table blogs(
	'id' varchar(50) not null,
	'user_id' varchar(50) not null,
	'user_name' varcharD(50) not null,
	'user_image' varchar(500) not null,
	'name' varchar(50) not null,
	'summary' varchar(200) not null,
	'content' mediumtext not null,
	'created_at' real not null,
	key 'idx_created_at' ('created_at')
	primary_key('id')
) engine = innodb default charset = utf-8;

create table comments(
	'id' varchar(50) not null,
	'blog_id' varchar(50) not null,
	'user_name' varcharD(50) not null,
	'user_image' varchar(500) not null,
	'user_name' varchar(50) not null,
	'content' mediumtext not null,
	'created_at' real not null,
	key 'idx_created_at' ('created_at')
	primary_key('id')
)  engine = innodb default charset = utf-8;

# test_db.py

from models import User,Blog,Comment
from transwarp import db

db.create_engine(user = 'www-data',password = 'www-data',database = 'awesome')

u = User(name = 'Test',email = 'test@example.com',password = '1234567890',image = 'about:blank')

u.insert()

print 'new user id:',u.id

u1 = User.find_first('where email = ?','test@example.com')
print 'find user\'s name:',u1.name

u1.delete()

u2 = User.find_first('where email = ?','test@example')
print 'find user:',u2 