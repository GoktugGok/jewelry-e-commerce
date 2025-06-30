// --- Favori kalpler (hearts) seçiliyor ---
const hearts = document.querySelectorAll('[id^="heart-"]');

// Her kalbe tıklandığında favori durumunu değiştir
hearts.forEach((heart) => {
    heart.addEventListener("click", function(event) {
        const productId = heart.id;
        event.stopPropagation(); // Tıklamanın yukarı gitmesini önle
        if (heart.classList.contains('bi-heart')) {
            // Boş kalp -> dolu kalp yap
            heart.classList.remove('bi-heart'); 
            heart.classList.add('bi-heart-fill');
            setCookie(productId, 'filled', 7); // 7 gün favoride tut
        } else {
            // Dolu kalp -> boş kalp yap
            heart.classList.remove('bi-heart-fill');
            heart.classList.add('bi-heart');
            setCookie(productId,'empty',-1); // Çerez sil
        }
    });
});

// Çerez ayarlama fonksiyonu
function setCookie(name,value,days){
    const expires = days ? `; expires=${new Date(Date.now() + days * 864e5).toUTCString()}` : '';
    document.cookie = `${name}=${value}${expires}; path=/`;
}

// Çerezden değer okuma fonksiyonu
function getCookie(name){
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

// Sayfa yüklendiğinde favori kalpleri çerezden kontrol edip uygun ikona geçir
window.onload = function(){
    hearts.forEach((heart) => {
        const cookieValue = getCookie(heart.id);
        if(cookieValue === 'filled'){
            heart.classList.remove('bi-heart');
            heart.classList.add('bi-heart-fill');
        } else {
            heart.classList.remove('bi-heart-fill');
            heart.classList.add('bi-heart');
        }
    });
}

// --- Ürün görseli değiştir ve fiyat güncelle ---
// Fare ile farklı metal üzerine gelince
function changeMainImage(productId, newImageUrl, newPrice, check) {
    const mainImage = document.getElementById(`product-image-${productId}`);
    const priceElement = document.getElementById(`product-price-${productId}`);
    if (mainImage) {
        // Orijinal resim url'sini sakla (ilk defa)
        if (!mainImage.dataset.originalSrc) mainImage.dataset.originalSrc = mainImage.src;
        mainImage.src = newImageUrl; // Yeni görseli ayarla
        if (priceElement && newPrice) {
            // Orijinal fiyatı sakla (ilk defa)
            if (!priceElement.dataset.originalPrice) priceElement.dataset.originalPrice = priceElement.textContent;
            priceElement.textContent = `${newPrice} TL`; // Yeni fiyatı göster
        }
        if (check) check.classList.add('checked'); // İlgili kutucuğu işaretle
    }
}

// Fare metal üzerinden çekilince orijinal görsel ve fiyatı geri yükle
function resetMainImage(productId, originalImageUrl, originalPrice, check) {
    const mainImage = document.getElementById(`product-image-${productId}`);
    const priceElement = document.getElementById(`product-price-${productId}`);
    if (mainImage && mainImage.dataset.originalSrc) {
        mainImage.src = originalImageUrl; // Orijinal resmi koy
        if (priceElement && priceElement.dataset.originalPrice) {
            priceElement.textContent = `${originalPrice} TL`; // Orijinal fiyatı koy
        }
        if (check) check.classList.remove('checked'); // Kutucuğu kaldır
    }
}

// --- Filtreleme checkbox'ları ---
const checkboxes = document.querySelectorAll('input[type="checkbox"]');

// Filtreli ürün adlarının gösterileceği containerlar
const filterList = document.getElementById('filterList');
const filterListM = document.getElementById('filterListM');
const filterContainer = document.getElementById('filters');
const filterContainerM = document.getElementById('filtersM');

// Her checkbox değiştiğinde filtre listesini güncelle
checkboxes.forEach(checkbox => {
    checkbox.addEventListener('change', updateFilterList);
});

// Filtreli seçimlerin listesini güncelleyen fonksiyon
function updateFilterList() {
    // Önce listeleri temizle
    filterList.innerHTML = '';
    filterListM.innerHTML = '';

    let hasChecked = false; // En az bir seçim var mı kontrolü

    checkboxes.forEach(checkbox => {
        if (checkbox.checked) {
            hasChecked = true;
            let label = '';

            // Label'ı bulmak için farklı durumları kontrol et
            if (checkbox.nextElementSibling && checkbox.nextElementSibling.querySelector('.Text')) {
                label = checkbox.nextElementSibling.querySelector('.Text').textContent;
            } else if (checkbox.classList.contains('Color')) {
                label = checkbox.closest('div').querySelector('.fake-checkbox').textContent.trim();
            } else if (checkbox.classList.contains('Size')) {
                label = checkbox.closest('label').querySelector('.box').textContent.trim();
            }

            // Seçilen filtreyi hem desktop hem mobil listelere ekle
            const itemHtml = `
                <div class="col-md-2 col-sm-3 col-lg-4 col-6 d-flex justify-content-center align-items-center border border-1 rounded-5">
                    <div class="small">${label}</div>
                    <i class="p-0 m-0 bi bi-x mt-1"></i>
                </div>
            `;

            filterList.innerHTML += itemHtml;
            filterListM.innerHTML += itemHtml;
        }
    });

    // Eğer en az bir filtre seçildiyse filtre kutusunu göster, yoksa gizle
    filterContainer.style.display = hasChecked ? 'block' : 'none';
    filterContainerM.style.display = hasChecked ? 'block' : 'none';
}

// --- Tüm filtreleri temizle butonları ---
document.getElementById('FilterAllDeleteM').addEventListener('click', () => {
    uncheckAllChecked();
    filterContainerM.style.display = 'none';
    filterList.innerHTML = '';
    filterListM.innerHTML = '';
});
document.getElementById('FilterAllDeleteC').addEventListener('click', () => {
    uncheckAllChecked();
    filterContainer.style.display = 'none';
    filterList.innerHTML = '';
    filterListM.innerHTML = '';
});

// Checkboxların hepsini işaretsiz hale getir
function uncheckAllChecked() {
    checkboxes.forEach(checkbox => checkbox.checked = false);
}
