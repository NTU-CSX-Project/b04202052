# b04202052
進階軟體開發專題

# YOLO影片物件標誌
使用YOLO套件與OpenCV標誌影片中的物件。
# Titanic
架設簡易NET並預測船上乘客於船難後是否存活。  
>**EDA**  
>1. 此次分析所採用的資料分別為船艙等級、性別、年齡、兄弟姊妹數量、父母與子女數量、票價、登船地點、救生船編號。以上是經過組內討論後，決定採用的資料。  
>2. 其中有經過轉換與處理的資料分別為性別、年紀、登船地點、救生船。  
>3. 其中性別的量化方法為「女生=1，男生=0」。  
>4.	年紀有經過處理的原因為並非每組資料都有年紀這筆資料，而我們對年紀的處理方法為隨機給沒有年紀的資料一個整數值，作為其年紀，又這個隨機取值的範圍在原始資料的最大值與最小值之間。  
>5.	經過查詢後，我們發現原始資料中，登船地點的「S」、「C」與「Q」分別代表著「Southampton」、「Cherbourg」、「Queenstown」。數值化的方法為按照鐵達尼號當時行駛的順序來制定，其中「Southampton=1，Cherbourg=2，Queenstown=3」。  
>6.	救生船編號經觀察後，發現若是搭乘數字編號的救生艇，艇上人員基本上都有存活，但是若救生艇編號為英文字母的話，則不一定存活，所以我們數值化的方法為定「救生艇為數字編號=2，救生艇為英文編號=1，沒有搭到救生艇=0」。

>**NET**
>![image](https://github.com/NTU-CSX-Project/b04202052/blob/master/NET.png)


# LSTM
>**LSTM Report**  
>介紹encoder-decorder LSTM。

>**CPU Usage Prediction**  
>以舊有六台電腦的資料預測每一次CPU使用率的相對高峰，並且將這六台電腦的資料作為樣本，去製作出一個可預測新客戶電腦CPU使用率高峰時間的model。
>>**EDA**  
>>1. 這各個項目中，我只取用了CPU使用率與時間，因為我認為這是最直接可以知道一台電腦被使用狀況的數值。  
>>2. 為了區別不同的電腦，我分別給不同ID的電腦一個數字做代表，附表是電腦代號與ID的對照表。而這個給數字的依據是按照各台電腦CPU使用率突然有落差的次數多寡來給分的，如果落差次數越多，分數越高。  
>>3. 因為時間只有一小段區間，所以我認為日期並不重要，但是是在一天中的哪一天有usage gap的情況就很重要，所以我也有把時間給納入考量。另外，為了方便計量，我以每天的凌晨12點為基準點，以秒為單位將每組資料的時間做換算。  
>>4. 我機台出現usage gap時，前後一段時間的CPU使用率可能會反映出一些特徵，所以我也一併把出現usage gap的前後10筆資料一起抓出來。  
>>5. 最後，我給每秒鐘機台的使用狀況訂了一個表現的分數，而我的model在預測的也是這個分數。這個分數是這樣訂的，他等於標準化後的CPU使用率與兩倍的標準化CPU使用率變化和。  
>>  
>>  
>>電腦代號與ID的對照表

>>|             電腦使用者ID            | 電腦數字代號 |  
>>|:---------------------------------:|:----------:|  
>>| b-956223090-UserCluster1-sysadmin |     6      |  
>>| t-657740490-UserCluster1-sysadmin |     5      |  
>>| i-325376172-UserCluster1-sysadmin |     4      |  
>>| c-959255288-UserCluster1-sysadmin |     3      |  
>>| b-956223090-UserCluster1-sysadmin |     2      |  
>>| a-957043145-UserCluster1-sysadmin |     1      |

>>**LSTM NET**  
>>參考資料：  
>>[1]https://machinelearningmastery.com/convert-time-series-supervised-learning-problem-python/  
>>[2]https://goo.gl/NcGzAJ  

# NLP
使用SnowNLP與Jieba判斷歌曲是首開心或不開心的歌，另外同時使用Jieba提取歌詞內的關鍵字句。


