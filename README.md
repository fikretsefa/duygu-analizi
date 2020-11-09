Aws boto3 ile tercüme ve duygu analizi

Çalışmada aws boto3 kullanılarak girilen verinin önce **batch_detect_dominant_language** ile dil algılanması amaçlanmıştır. Algılanan dil **detect_sentiment** tarafından destekleniyorsa tercüme edilmeden duygu analiz tahmini yapılmıştır. Desteklenmeyen bir dil ise **translate_text** ile İngilizce tercüme edilip sonrasında tahminleme yapılmıştır.

![](https://media.giphy.com/media/jKGh2Ivl4WKunZzhbU/giphy.gif)

*Türkçe **detect_sentiment** tarafından desteklenmemektedir. Bu nedenle Türkçe veriler **TurkishNLP** ile hataların giderilmesi ve noktalama düzeltilmesi yapılmıştır. Daha sonrasında duygu analizi tespiti gerçekleştirilmiştir.

![](https://media.giphy.com/media/qEkkqpew7rHG6OJpoZ/giphy.gif)


