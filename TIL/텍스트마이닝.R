library(tm)
library(topicmodels)
library(plyr)
library(ggplot2)

setwd('C:/Users/tjy22/Desktop/2021-2 강의자료/빅자분/빅데이터 분석_그것이 R고 싶다(임동훈)/빅데이터 분석_그것이 R고 싶다(임동훈)/제4장')
pos.words = scan('positive-words.txt', what='character', comment.char=';')
neg.words = scan('negative-words.txt', what='character', comment.char=';')

setwd('C:/Users/tjy22/Downloads/C50/C50train')

dir <- data.frame(Reporter=0,result=0)

for (i in list.files()) {
  A <- DirSource(directory = i)
  
  corpus <- VCorpus(A)
  corpus <- tm_map(corpus, tolower)
  corpus <- tm_map(corpus, stripWhitespace)
  corpus <- tm_map(corpus, removePunctuation)
  corpus <- tm_map(corpus, removeNumbers)
  corpus <- tm_map(corpus, removeWords, stopwords('english'))
  
  corpus <- tm_map(corpus, stemDocument)
  corpus <- tm_map(corpus, PlainTextDocument)
  dtm <- DocumentTermMatrix(corpus) # 50 2099
  dtm <- dtm[,findFreqTerms(dtm,lowfreq=10)]

  
  DTM <- as.data.frame(as.matrix(dtm))
  
  pos.matches <- match(colnames(DTM),pos.words)
  neg.matches <- match(colnames(DTM),neg.words)
  
  pos.matches = !is.na(pos.matches)
  neg.matches = !is.na(neg.matches)
  
  pos.DTM <- DTM[,pos.matches]
  neg.DTM <- DTM[,neg.matches]

  res <- data.frame(pos.DTM = rowSums(pos.DTM), neg.DTM = rowSums(neg.DTM),row.names = rownames(DTM))
  res$sum <- res$pos.DTM - res$neg.DTM
  result <- ifelse(res$sum > 3, 1, ifelse(res$sum < -3, -1, 0))
  
  t <- c(i, sum(result))
  dir <- rbind(dir, t)
}

df <- dir[-1,]
df$result <- as.numeric(df$result)
df <- df[order(df$result), ]
rownames(df) <- 1:nrow(df)

class(as.numeric(rownames(df)))

ggplot(df,aes(x=result,y=reorder(Reporter, -result), fill=as.numeric(rownames(df))))+
  geom_bar(stat="identity") + geom_col()

