# Filter missing values, redundant, interdependent and artrichary features from kaggle. 
a=read.csv("~/Downloads/CSE6242_Project/data/Zillow/properties_2016_filter.csv")
b=read.csv("train_2016_v2.csv")
a1=a[a[,1]%in%b[,1],]
write.table(a1,"2016_properties_60000.csv",sep=",",quote=F,row.names=F,na="")
c=read.csv("2016_properties_60000.csv")

nacount= vector(length=57)
for(i in 1:57) {
	nacount[i]=length(a1[is.na(a1[,i+1]),1])
}
names(nacount)=colnames(a)[2:58]
nacount=nacount[order(nacount)]
nacountp=nacount/nrow(a1)*100
pdf("missing_value.pdf",height=10,width=6)
par(mar=c(5,12,1,1))
barplot(nacountp,names.arg=names(nacountp),horiz=T,las=2,xlim=c(0,100),xlab="Percent of missing values")
dev.off()

name = names(nacountp[nacountp<50])
a2=a1[,colnames(a1)%in%c(name,"parcelid")]
a2=a2[,-which(colnames(a2)%in%c("assessmentyear","unitcnt","propertylandusetypeid","calculatedbathnbr","fullbathcnt","finishedsquarefeet12","regionidcounty","regionidcounty","fips","structuretaxvaluedollarcnt","landtaxvaluedollarcnt","taxamount","fireplaceflag","axdelinquencyflag","hashottuborspa"))]
a3=a2[,-which(colnames(a2)%in%c("buildingqualitytypeid","heatingorsystemtypeid"))]
a4=na.exclude(a3)
a5=a2[a2[,1]%in%a4[,1],]
write.table(a5,"2016_properties_60000.csv",sep=",",quote=F,row.names=F,na="")

name=name[order(name)]
temp=na.exclude(a[,colnames(a)%in%c("taxvaluedollarcnt","landtaxvaluedollarcnt")])
cor(temp[,1],temp[,2])
mi.empirical(temp)

#clustering and refill
heating=matrix(nrow=nrow(c),ncol=3)
quality=matrix(nrow=nrow(c),ncol=4)
for(i in 1:nrow(heating)){
	if(is.na(c[i,6])){
		heating[i,1]=0
		heating[i,2]=0
		heating[i,3]=0
	}
	else if(c[i,6]==2){
		heating[i,1]=1
		heating[i,2]=0
		heating[i,3]=0
	} else if(c[i,6]==6){
		heating[i,1]=0
		heating[i,2]=1
		heating[i,3]=0
	} else if(c[i,6]==7){
		heating[i,1]=0
		heating[i,2]=0
		heating[i,3]=1
	}else{
		heating[i,1]=0
		heating[i,2]=0
		heating[i,3]=0
	}
	if(is.na(c[i,4])){
		quality[i,1]=0
		quality[i,2]=0
		quality[i,3]=0
		quality[i,4]=0
	}
	else if(c[i,4]==1){
		quality[i,1]=1
		quality[i,2]=0
		quality[i,3]=0
		quality[i,4]=0
	} else if(c[i,4]==4){
		quality[i,1]=0
		quality[i,2]=1
		quality[i,3]=0
		quality[i,4]=0
	} else if(c[i,4]==7){
		quality[i,1]=0
		quality[i,2]=0
		quality[i,3]=1
		quality[i,4]=0
	}else if(c[i,4]%in%c(6,8,10,11,12)){
		quality[i,1]=0
		quality[i,2]=0
		quality[i,3]=0
		quality[i,4]=1
	}else{
		quality[i,1]=0
		quality[i,2]=0
		quality[i,3]=0
		quality[i,4]=0
		}
}

c=cbind(c,heating,quality)
c=c[,-c(4,6)]
c=c[,-17]
colnames(c)[17:23]=c("heating1","heating2","heating3","quality1","quality2","quality3","quality4")
write.table(c,"2016_properties_60000v2.csv",sep=",",quote=F,row.names=F,na="")

# Generate training and testing data
d=read.csv("2016_properties_60000v2.csv")
train_id=sample(nrow(d),round(nrow(d)*0.8))
d_train=d[train_id,]
d_test=d[-train_id,]
write.table(d_train,"2016_properties_60000v2_train.csv",sep=",",quote=F,row.names=F,na="")
write.table(d_test,"2016_properties_60000v2_test.csv",sep=",",quote=F,row.names=F,na="")

# Incorporate and transform environmental information
env=read.csv("all_environmental1.csv")
train=read.csv("2016_properties_60000v2_train.csv")
test=read.csv("2016_properties_60000v2_test.csv")
zip=read.csv("2016_addr_zip_60000.csv")
env1=aggregate(env,by=list(env[,1]),mean)
house=vector(length=nrow(env))
pop=vector(length=nrow(env))
for(i in 1:nrow(env)){
	temp=unlist(strsplit(as.character(env[i,5]),","))
	temp1=""
	for(j in 1:length(temp)){
		temp1=paste(temp1,temp[j],sep="")
	}
	house[i]=as.numeric(temp1)
	temp=unlist(strsplit(as.character(env[i,6]),","))
	temp1=""
	for(j in 1:length(temp)){
		temp1=paste(temp1,temp[j],sep="")
	}
	pop[i]=as.numeric(temp1)
}
env[,5]=house
env[,6]=pop
env1=na.exclude(env)
env2=aggregate(env1,by=list(env1[,1]),mean)
env2=env2[,2:ncol(env2)]
train1=merge(train,zip,by=1)
train1$regionidzip=train1$zipcode
train2=train1[,1:23]

test1=merge(test,zip,by=1)
test1$regionidzip=test1$zipcode
test2=test1[,1:23]

train3=merge(train2,env2,by.x=12,by.y=1)
train3=train3[,2:ncol(train3)]
test3=merge(test2,env2,by.x=12,by.y=1)
test3=test3[,2:ncol(test3)]
write.table(train3,"2016_properties_60000v3_train.csv",sep=",",quote=F,row.names=F,na="")
write.table(test3,"2016_properties_60000v3_test.csv",sep=",",quote=F,row.names=F,na="")

# Visualization of prediction results.
#error = rbind(c(2.35,2.35,2.5,3.87,2.78),c(2.01,2.01,2.42,4.25,2.36))
error = rbind(c(2.19,2.35,2.5,3.87,2.78,2.47,2.23),c(2.01,2.01,2.42,4.25,2.36,2.33,2.04))

pdf("error.pdf",width=4,height=4)
barplot(error,beside=T,col=c(2,4))
legend("topleft",c("ori","expanded"),pch=15,col=c(2,4),bty='n')
dev.off()

#score = rbind(c(0.438,0.438,0.402,0.073,0.335),c(0.518,0.519,0.422,-0.018,0.433))
score = rbind(c(0.475,0.438,0.402,0.073,0.335,0.409),c(0.518,0.519,0.422,-0.018,0.433,0.441))

pdf("score.pdf",width=4,height=4)
barplot(score,beside=T,col=c(2,4))
legend("topright",c("ori","expanded"),pch=15,col=c(2,4),bty='n')
dev.off()

train4=read.csv("train_v4.csv",header=T)
test4=read.csv("test_v4.csv",header=T)
total4=rbind(train4,test4)
total5=total4[,c(2,37)]
a1=a[a[,1]%in%total5[,1],]
a2=merge(a1,zip,by=1)
a2$regionidzip=a2$zipcode
a3=merge(a2,env2,by.x=ncol(a2),by.y=1)
a4=merge(a3,total5,by.x=2,by.y=1)
write.table(a4,"visualization.txt",quote=F,na="",sep="\t")

# Feature importance
feat=read.table("feature_importance.txt",sep="\t")
pdf("Feature_small.pdf",width=5,height=5)
barplot(feat[1:10,2],names.arg=feat[1:10,1],col=1:10,las=2)
dev.off()
pdf("Feature_large.pdf",width=5,height=5)
barplot(feat[11:20,2],names.arg=feat[11:20,1],col=1:10,las=2)
dev.off()