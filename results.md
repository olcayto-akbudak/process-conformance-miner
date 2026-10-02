# Çalıştırılmış kabul sonuçları

Python 3.12.14, sentetik `scenario.json`; yerel test sayısı **8**, tümü başarılı. Ham test günlüğü `test-log.txt`.

Fit oranı %50.0; 2 süreç varyantı.

Sonuçlar yalnız bu örneğe aittir; üretim doğruluğu veya performans garantisi olarak yorumlanmamalıdır. Ölçülen iş sonucunu kontrol edin; örnek negatif vaka içeriyorsa ret beklenir. Tam çıktı `sample-report.json`.

## Sınanan davranışlar

| Test | Kontrol |
|---|---|
| `test_parallel` | parallel |
| `test_missing` | missing |
| `test_unknown` | unknown |
| `test_incomplete` | incomplete |
| `test_duplicate_cases` | duplicate cases |
| `test_bad_arc` | bad arc |
| `test_negative_marking` | negative marking |
| `test_duplicate_activity` | duplicate activity |

## Gelişmiş deney planı

1. Petri nete ret/düzeltme döngüsü ekleyin ve varyantları karşılaştırın.
2. Token replay ile minimum maliyet alignment sonuçlarını aynı logda kıyaslayın.
3. Süre ve görevli ayrılığı kurallarını olay zamanları üzerinden ekleyin.
4. Fitness değeri yüksek ama final marking hatalı izleri ayrıca raporlayın.
