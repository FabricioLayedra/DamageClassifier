#library(caret)
setwd("/home/belen/github/DamageClassifier/scripts/")

set.seed(12345)
df.scale = read.csv("../data/features_parroquia_normalized.csv", sep=",", as.is=TRUE, header=TRUE)

#supressMessages()
df.scale$population <- NULL
df.scale$damage_ratio = NULL
df.scale$total_houses = NULL
df.scale$parroquia = NULL

#centering, scaling of input features
#df.scale<-cbind(scale(df[1:13]),df[14])

#do data partitioning
#inTrain<-createDataPartition(y=house.scale$medv ,p=0.70, list=FALSE)
#train.data <- house.scale[inTrain,]
#test.data <- house.scale[-inTrain]

inTrain = sample(1:nrow(df.scale),dim(df.scale)[1]*0.80)
train.data = df.scale[inTrain,]
test.data = df.scale[-inTrain,]


#modelo lineal
set.seed(1234)
reg <- lm(damaged_houses ~ ., data = train.data)
summary(reg)
tr<- data.frame(train.data$damaged_houses, reg$fitted.values, reg$residuals)
head(tr)

#prediccion 
pred_training <- predict(reg, newdata = test.data)
vl.res <- data.frame(test.data$damaged_houses, pred_training, residuals = test.data$damaged_houses - pred_training)
head(vl.res)

library(forecast)
#compute accuracy on training test
#accuracy(exp(reg$fitted.values),train.data$damaged_houses)

#compute error for test
accuracy(pred, test.data$damaged_houses)

"
Xtrain = train.data[,-6]
ytrain = train.data[,6]
Xtest = test.data[,-6]
ytest = test.data[,6]

#Ridge regression
library(glmnet)
#multinomial with ridge regression
model <- cv.glmnet(Xtrain, ytrain,family = 'multinomial', alpha = 1, nfolds=3, standardize=TRUE)
#predict
predNumbers <- predict(model,Xtest,type='response', s=model$lambda.min)
#accuracy
conf_mat <- table(predNumbers,ytest)
acc <- sum(diag(conf_mat)) / nrow(test.data)
acc
"
