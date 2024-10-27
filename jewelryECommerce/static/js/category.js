
var offheart = document.getElementById('heart');
    
offheart.addEventListener("click", function(){
    // Kalp dolu ve boş ikonları arasında geçiş yap
    if (offheart.classList.contains('bi-heart')) {
        offheart.classList.remove('bi-heart'); // Boş kalp sınıfını kaldır
        offheart.classList.add('bi-heart-fill'); // Dolu kalp sınıfını ekle
    } else {
        offheart.classList.remove('bi-heart-fill'); // Dolu kalp sınıfını kaldır
        offheart.classList.add('bi-heart'); // Boş kalp sınıfını ekle
    }
});

    function toggleCheckbox(element) {
        // Label elementine ulaşmak için parentNode kullanıyoruz
        const label = element.parentNode;
        // Eğer checkbox seçiliyse checked class'ı ekle, değilse kaldır
        if (element.checked) {
            label.classList.add('checked');
        } else {
            label.classList.remove('checked');
        }
    }
        document.querySelectorAll('input[type="checkbox"]').forEach((checkbox) => {
        checkbox.addEventListener('change', (event) => {
        if (event.target.checked) {
            console.log(`${event.target.nextElementSibling.textContent.trim()} selected!`);
        } else {
                console.log(`${event.target.nextElementSibling.textContent.trim()} deselected!`);
            }
        });
    });
const checkboxes = document.querySelectorAll('input[type="checkbox"]');
const filterList = document.getElementById('filterList');
const filterContainer = document.getElementById('filters');

const filterListM = document.getElementById('filterListM');
const filterContainerM = document.getElementById('filtersM');

checkboxes.forEach(checkbox => {
    checkbox.addEventListener('change', function () {
        updateFilterList();
    });
});

function updateFilterList() {
    // Listeyi sıfırlıyoruz
    filterList.innerHTML = '';
    filterListM.innerHTML = '';  // Mobil listeyi de sıfırlıyoruz
    let hasChecked = false; // Kontrol işareti olup olmadığını takip ediyoruz

    checkboxes.forEach(checkbox => {
        if (checkbox.checked) {
            hasChecked = true;
            let label = ''; // Label değerini dışarıda tanımlıyoruz

            // Önce .Text olan label'ı kontrol et
            if (checkbox.nextElementSibling && checkbox.nextElementSibling.querySelector('.Text')) {
                label = checkbox.nextElementSibling.querySelector('.Text').textContent;
                console.log("Normal checkbox label: ", label); // Kontrol amaçlı
            }
            // Eğer .Text yoksa, .fake-checkbox'u kontrol et
            else if (checkbox.classList.contains('Color')) {
                label = checkbox.closest('div').querySelector('.fake-checkbox').textContent.trim();
                console.log("Resimli checkbox label:", label); // Kontrol amaçlı
            }
            else if (checkbox.classList.contains('Size')) {
                const closestLabel = checkbox.closest('label');
                label = closestLabel.querySelector('.box').textContent.trim();
            }
            // Eğer ne .Text ne de .fake-checkbox yoksa
            else {
                console.log("Ne .Text ne de .fake-checkbox bulunamadı!"); // Kontrol amaçlı
            }

            // Ekran boyutuna göre uygun listeye yeni eleman ekliyoruz
            if (window.innerWidth < 991) {
                filterListM.innerHTML += `
                <div class="col-md-2 col-sm-3 col-lg-4 col-6 d-flex justify-content-center align-items-center border border-1 rounded-5">
                    <div class="small">${label}</div>
                    <i class="p-0 m-0 bi bi-x mt-1"></i>
                </div>
                `;
                filterList.innerHTML += `
                <div class="col-md-2 col-sm-3 col-lg-4 col-6 d-flex justify-content-center align-items-center border border-1 rounded-5">
                    <div class="small">${label}</div>
                    <i class="p-0 m-0 bi bi-x mt-1"></i>
                </div>
                `;
            } else {
                filterList.innerHTML += `
                <div class="col-md-2 col-sm-3 col-lg-4 col-6 d-flex justify-content-center align-items-center border border-1 rounded-5">
                    <div class="small">${label}</div>
                    <i class="p-0 m-0 bi bi-x mt-1"></i>
                </div>
                `;
                filterListM.innerHTML += `
                <div class="col-md-2 col-sm-3 col-lg-4 col-6 d-flex justify-content-center align-items-center border border-1 rounded-5">
                    <div class="small">${label}</div>
                    <i class="p-0 m-0 bi bi-x mt-1"></i>
                </div>
                `;
            }
        }
    });

    // Eğer en az bir checkbox seçildiyse filtreleme alanını göster
    if (hasChecked) {
        filterContainer.style.display = 'block';
        filterContainerM.style.display = 'block'; // Mobil konteyneri de göster
    } else {
        filterContainer.style.display = 'none';
        filterContainerM.style.display = 'none'; // Mobil konteyneri de gizle
    }
}

document.getElementById('FilterAllDeleteM').addEventListener('click', function(){
    uncheckAllChecked();
    filterContainerM.style.display = 'none';
    filterList.innerHTML = '';
    filterListM.innerHTML = '';
})
document.getElementById('FilterAllDeleteC').addEventListener('click', function(){
    uncheckAllChecked();
    filterContainer.style.display = 'none';
    filterList.innerHTML = '';
    filterListM.innerHTML = '';
})
function uncheckAllChecked() {
    checkboxes.forEach(checkbox => {
        if (checkbox.checked) {
            checkbox.checked = false;
        }
    });
}


