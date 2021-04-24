import time 


# Sonucun alınması için for döngüsünün tamamlanmasını bekler
# Memory de result değişkeni yer kaplar ve yüksek boyutlu işlevlerde sistem kısa sürede tükenir 
def compute():
    result = []
    
    for i in range(10):
        time.sleep(0.5)
        result.append(i**3)
        
    return result


# Her bir for döngüsüde oluşan veriyi yield aracılığı ile bir nevi return eder
# Değiken ataması olmadığı için sistemde yer kaplamaz anlık veri tutar ve gönderir
# Anlık çalışmasından dolayı daha hızlı çalışır 
def compute2():
    for i in range(10):
        time.sleep(0.5)
        yield i**3
    

# print işlevi yield func ile kullanılmaz 
print(compute2()) # output: <generator object compute2 at 0x7f5523cf6c10>

# compute2() den gönderilen her bir değeri for döngüsü aracılığı ile gerçek zamanda alıyoruz 
for res in compute2():
    print(res)



