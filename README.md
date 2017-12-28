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


