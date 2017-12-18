var bla = [];

$(document).ready(function () {
    loadPapers();


    function useReturnData(data) {
        myvar = data.papers;
        var url = ''
        var id = '';
        $.each(myvar, function (key, paper) {
            id = paper.id;
            $('.mypapers .list ').append(" <li class='cf '> <div class='content'>" + paper.id + "<h4>" +
                paper.title + "<span class='status'>" + paper.status+ "</span>" +"</h4><br>" + paper.abstract + "<br>" + "<br>" +
                "<a href='api/paper/"+id+"'> <button class='btn orange'>Show</button></a>"+
                "<a href='api/paper/delete/"+id+"'> <button class='btn orange'>Delete</button></a>"+
                "</a> "  + "</form><br>" +"</a>" + "</div></li>");
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
