const modalWrapper = document.querySelector('.modal-wrapper');
const images = document.querySelectorAll('.image');
const modalImage = document.querySelector('.modal-image');

images.forEach(function(image) {
     image.addEventListener('click', function() {
          modalWrapper.classList.add('show');
          modalImage.classList.add('show');

          var imageSrc = image.getAttribute('data-src');
          modalImage.src = imageSrc;
     });
});

modalWrapper.addEventListener('click', function() {
     if (this.classList.contains('show')) {
          this.classList.remove('show');
          modalImage.classList.remove('show');
     }
});

function getcurrdata() {
     $.ajax({
         type: 'POST',
         url: '/people',
         people: '',
         contentType: 'application/json'
     })
     .done( (people) => {
         // データ取得成功
         console.log("success");
         // JSONからデータ抽出
         var json_data = JSON.parse(people.Result);
         const j_merged_num = json_data.j_merged_num;
         const z_merged_num = json_data.z_merged_num;

         if (j_merged_num < 60 && j_merged_num >= 0) {
             $("#j_merged_num").attr("src", "../static/images/empty.png");
         } else if (j_merged_num < 80 && j_merged_num >= 60) {
             $("#j_merged_num").attr("src", "../static/images/little_empty.png");
         } else if (j_merged_num < 1000 && j_merged_num >= 80) {
             $("#j_merged_num").attr("src", "../static/images/crowded.png");
         } else {
             $("#j_merged_num").html("Sorry...No Content");
         }

         $("#h2_j_merged_num").html("推定人数：" + j_merged_num);

         if (z_merged_num < 60 && z_merged_num >= 0) {
             $("#z_merged_num").attr("src", "../static/images/empty.png");
         } else if (z_merged_num < 80 && z_merged_num >= 60) {
             $("#z_merged_num").attr("src", "../static/images/little_empty.png");
         } else if (z_merged_num < 1000 && z_merged_num >= 80) {
             $("#z_merged_num").attr("src", "../static/images/crowded.png");
         } else {
             $("#z_merged_num").html("Sorry...No Content");
         }

         $("#h2_z_merged_num").html("推定人数：" + z_merged_num);
     })
     .fail( (people) => {
         console.log("error");
     });
  }