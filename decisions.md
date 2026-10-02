# Tasarım kararları

## Alan motorunu CLI'dan ayırmak

`run(config)` orkestrasyonu kaynak kodun doğrudan test edilebilmesini sağlar. JSON arayüz taşınabilirliği artırır; bu sürüm kullanıcı arayüzü barındırmaz.

## Seçilen yöntem

Petri net token replay, paralel adımlar. Eksik giriş jetonları sanal olarak eklenir ve ihlal sayılır; sonuç fit bayrağı ve fitness birlikte okunur.

## Bilinçli sınır

Optimal alignment algoritması değildir; zaman ve kaynak kuralları ayrıca modellenmelidir.

## Önerilen sonraki doğrulama

Gerçek kullanım hacmiyle testten önce mevcut kabul ve ret örneklerinin alan uzmanı tarafından onaylanması gerekir. Sonraki sürüm performans ölçümleri, dış adaptör sözleşmesi ve üretim gözlemlenebilirliğini ayrı karar kayıtlarında ele almalıdır.
