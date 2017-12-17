    var bla = [];

$(document).ready(function () {
  loadPapers();
    

function loadPapers(c) {
	if (c) {
		$.ajax({
			url: '/api/papers',
			method: 'get',
			dataType: 'json',
            success: function(data) {
                useReturnData(data);
                console.log(data);
    }
		})

	}
}



function useReturnData(data){
    myvar = data.papers;

     $.each(myvar, function(key, paper) {
         $('.list').append('<div>' + "<h4>" +
             paper.title + "</h4><br>" + paper.abstract +'</div><br>'); 
        console.log("My name is "+paper.title+" and I am a "+paper.abstract);
    });
};

function displayContent(d){
    $('.mypapers li').text(d.title);
}

});