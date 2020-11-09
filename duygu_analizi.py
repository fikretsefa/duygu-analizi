#boto3 aws kütüphanesidir.Cümle tahminlemesi, translate yapabilir.
#daha birçok boto3 servisi için dökümantasyon linkini takip edebilirsiniz.
#https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/index.html
import boto3
#string işlemlerinde whtespaceleri temizlemek için kullanıldı.
import string
#string işlemlerinde whtespaceleri temizlemek için kullanıldı.
import re
#türkçe yazım hatalarını düzeltmek amacıyla kullanıldı.
import detector
#words klasörünün içerisindeki word list ile veri seti oluşturulur.
obj = detector.TurkishNLP()
obj.create_word_set()
#boto3 translate servisi kullanılır.
boto3_translate = boto3.client(service_name='translate', use_ssl=True)
#boto3 comprehend servisi kullanılır.
boto3_comprehend = boto3.client(service_name='comprehend', use_ssl=True)
#boto3 comprehend servisinin destek verdiği dil kodlarını içerir.
detect_sentiment_language_code = ['en','es','fr','de','it','pt','ar','hi','ja','ko','zh','zh-TW']

#typoCorrection TurskıshNLP kullanarak yazım düzeltme işlemi gerçekleştirir.
def typoCorrection(input_text):
    sentence = obj.list_words(input_text)
    final_words = obj.auto_correct(sentence)
    final_sentence = " ".join(final_words)
    return final_sentence

#punctuation boşluk temizler ve noktalama işareti ekler.
#boto3 noktalamalara dikkat eder.
#cümle sonlarında nokta var ise doğruluk oranı artar.
def punctuation(input_text):
    removeWhiteSpace = re.sub(' +', ' ', input_text)
    removeLastWhiteSpace = removeWhiteSpace.rstrip();
    if removeLastWhiteSpace[-1] in string.punctuation:
        return removeLastWhiteSpace
    else:
        return removeLastWhiteSpace+"."

#boto3 ile dil algılama yapılır.
#algılanan dil kodu ve puanı geri döndürülür.
def batch_detect_dominant_language(input_text):
    input_text_array = [input_text]
    detect_language_result = boto3_comprehend.batch_detect_dominant_language(TextList=input_text_array)
    language_code = detect_language_result['ResultList'][0]['Languages'][0]['LanguageCode']
    language_score = detect_language_result['ResultList'][0]['Languages'][0]['Score']
    print('Detect Language Code : {}'.format(language_code))
    print('Detect Language Code Score : {}'.format(language_score))
    return language_code,language_score

#algılnan dil tercüme edilir.
def translate_text(input_text,SourceLanguageCode,TargetLanguageCode):
    translated_input = boto3_translate.translate_text(Text=input_text,SourceLanguageCode=SourceLanguageCode, TargetLanguageCode=TargetLanguageCode)
    translated_input_result = translated_input['TranslatedText']
    print('Translated Text : {}'.format(translated_input_result))
    return translated_input_result

#boto3 ile duygu analizi yapılır.
def comprehend(input_text,language_code):
    comprehend_result = boto3_comprehend.detect_sentiment(Text=input_text,LanguageCode=language_code)
    return comprehend_result

#analiz sonucu puanları ile görüntülenir.
def view_comprehend(comprehend_result):
    positive_score = comprehend_result['SentimentScore']['Positive']
    negative_score = comprehend_result['SentimentScore']['Negative']
    notr_score = comprehend_result['SentimentScore']['Neutral']
    print('Text is : {}'.format(comprehend_result['Sentiment']))
    print('Positive score : {}'.format(positive_score))
    print('Negative score : {}'.format(negative_score))
    print('Notr score : {}'.format(notr_score))

while True:
    print('')
    input_text = input("Enter Text : ")

    language_code,language_score = batch_detect_dominant_language(input_text)

    if(language_code in detect_sentiment_language_code):
        print('boto3 detect sentiment already supports this language: {}'.format(language_code))
        comprehend_result = comprehend(punctuation(input_text),language_code)
    else:
        print('boto3 detect sentiment does not support this language: {}'.format(language_code))
        if(language_code == 'tr'):
            translated_input_result = translate_text(typoCorrection(input_text),language_code,"en")
            comprehend_result = comprehend(punctuation(translated_input_result),"en")
        else:
            translated_input_result = translate_text(input_text,language_code,"en")
            comprehend_result = comprehend(punctuation(translated_input_result),"en")

    view_comprehend(comprehend_result)


