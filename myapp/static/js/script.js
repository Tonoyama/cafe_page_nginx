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
             $("#j-title").css("background-color","#9cc147");
         } else if (j_merged_num < 80 && j_merged_num >= 60) {
             $("#j_merged_num").attr("src", "../static/images/little_empty.png");
             $("#j-title").css("background-color","#FFC107");
         } else if (j_merged_num < 1000 && j_merged_num >= 80) {
             $("#j_merged_num").attr("src", "../static/images/crowded.png");
             $("#j-title").css("background-color","#f44336");
         } else {
             $("#j_merged_num").html("Sorry...No Content");
         }

         $("#h2_j_merged_num").html("推定人数：" + j_merged_num);

         if (z_merged_num < 60 && z_merged_num >= 0) {
             $("#z_merged_num").attr("src", "../static/images/empty.png");
             $("#z-title").css("background-color","#9cc147");
         } else if (z_merged_num < 80 && z_merged_num >= 60) {
             $("#z_merged_num").attr("src", "../static/images/little_empty.png");
             $("#z-title").css("background-color","#FFC107");
         } else if (z_merged_num < 1000 && z_merged_num >= 80) {
             $("#z_merged_num").attr("src", "../static/images/crowded.png");
             $("#z-title").css("background-color","#f44336");
         } else {
             $("#z_merged_num").html("Sorry...No Content");
         }

         $("#h2_z_merged_num").html("推定人数：" + z_merged_num);
     })
     .fail( (people) => {
         console.log("error");
     });
  }