var bla = [];

$(document).ready(function () {
    loadPapers();


    function useReturnData(data) {
        myvar = data.papers;

        $.each(myvar, function (key, paper) {
            $('.mypapers .list').append('<div>' + "<h4>" +
                paper.title + "</h4><br>" + paper.abstract + '</div><br>');
        });
    };


    function loadPapers() {
        $.ajax({
            url: '/api/papers',
            method: 'get',
            dataType: 'json',
            success: function (data) {
                useReturnData(data);
                console.log(data);
            }
        })


    }

});