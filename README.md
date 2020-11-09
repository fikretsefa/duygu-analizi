**Aws boto3 ile tercüme ve duygu analizi**

Duygu analizi, belirli bir metin parçasında ifade edilen görüşler gibi öznel bilgileri tanımlamak, çıkarmak veya karakterize etmek için kullanılan hesaplama ve doğal dil işleme tabanlı teknikler sınıfını ifade eder. Duygu analizinin temel amacı, bir yazarın çeşitli konulara yönelik tutumunu olumlu, olumsuz veya tarafsız kategorilere ayırmaktır.

Çalışmada aws boto3 kullanılarak girilen verinin önce **batch_detect_dominant_language** ile dil algılanması amaçlanmıştır. Algılanan dil **detect_sentiment** tarafından destekleniyorsa tercüme edilmeden duygu analiz tahmini yapılmıştır. Desteklenmeyen bir dil ise **translate_text** ile İngilizce tercüme edilip sonrasında tahminleme yapılmıştır.

![](https://media.giphy.com/media/jKGh2Ivl4WKunZzhbU/giphy.gif)

Türkçe **detect_sentiment** tarafından desteklenmemektedir. Bu nedenle Türkçe veriler **TurkishNLP** ile hataların giderilmesi ve noktalama düzeltilmesi yapılmıştır. Daha sonrasında duygu analizi tespiti gerçekleştirilmiştir.

<img src="https://media.giphy.com/media/qEkkqpew7rHG6OJpoZ/giphy.gif" width="280" >

**Boto3 Hakkında**
<br>
Boto3, Python geliştiricilerinin Amazon S3 ve Amazon EC2 gibi hizmetlerden yararlanan yazılımlar yazmasına olanak tanıyan, Python için Amazon Web Hizmetleri (AWS) Yazılım Geliştirme Kitidir (SDK). Desteklenen hizmetlerin listesi dahil olmak üzere güncel bilgileri <a target="_blank" href="https://boto3.amazonaws.com/v1/documentation/api/latest/index.html" >buradan</a> inceleyebilirsiniz.

