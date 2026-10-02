# Girdi ve çıktı sözleşmesi

UTF-8 JSON nesnesi; örnek dosya alanların tam iç içe yapısını gösterir. Zamanlar bu laboratuvarda sayısal sanal zaman/gün değeridir; saat dilimi dönüşümü yapılmaz.

| Üst alan | Tür | Örnek |
|---|---|---|
| `transitions` | `dict` | {'open': {'consume': {'start': 1}, 'produce': {'goods_wait': 1, 'invoice_wait': 1}}, 'goods': {'consume': {'goods_wait': 1}, 'produce': {'goods_done': 1}}, 'inv |
| `initial` | `dict` | {'start': 1} |
| `final` | `dict` | {'end': 1} |
| `cases` | `list` | [{'id': 'valid', 'trace': ['open', 'invoice', 'goods', 'pay']}, {'id': 'missing', 'trace': ['open', 'pay']}] |

## Semantik

Eksik giriş jetonları sanal olarak eklenir ve ihlal sayılır; sonuç fit bayrağı ve fitness birlikte okunur.

Alan motorunun doğrulamaları `app.py` içinde açıkça bulunur. Eksik zorunlu anahtarlar hata verir. Satır bazında karantina/bulgu üreten motorlar rapora yazar; yapısal konfigürasyon hataları işlemi keser. Tam JSON Schema dosyası bu sürümün kapsamında değildir.

## Çıktı

Gerçek çıktı şeması ve örnek değerler `sample-report.json` içinde yer alır. Örnek işleme özgü sonuçlar `results.md` içinde açıklanır. Dış tüketici alan adlarını ve birimleri değiştirmeden sözleşmeyi sürümlemelidir.
