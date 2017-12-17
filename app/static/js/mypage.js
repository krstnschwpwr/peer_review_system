var bla = [];

$(document).ready(function () {
    loadPapers();


    function useReturnData(data) {
        myvar = data.papers;

        $.each(myvar, function (key, paper) {
            $('.mypapers .list ').append("<li class='cf'><div class='content'>" + "<h4>" +
                paper.title + "<span class='status'>" + paper.status+ "</span>" +"</h4><br>" + paper.abstract + "<br>" + "<br>" +
                " <a href='{{ url_for('update_page') }}'> <button class='btn orange'>Edit</button>"+
                "</a> " + "<a href='/paper/delete/<int:paper_id>'>"
                + "<button class='btn' type='submit'>Delete</button> </form>"+
                "</a><br>"
                +"</a>" + "</div></li>");
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