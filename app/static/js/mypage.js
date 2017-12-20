var bla = [];

$(document).ready(function () {
    loadPapers();


    function useReturnData(data) {
        myvar = data.papers;
        var url = '';
        var id = '';
        $.each(myvar, function (key, paper) {
            id = paper.id;
            $('.mypapers .columns ').append(" <div class='column'><div class='box'> <article class='media'> "+
                "<div class='media-content clearfix'> <div class='content'> <small>" + paper.status + "</small>"+
                                "<h4 class='subtitle is-5'>" + paper.title+ " </h4><br>" + paper.abstract + "</p> </div>"+
                            "<div class='column is-narrow'></div> <a  class='button button is-link is-rounded' href='api/paper/"+id+"'>Show</a>"+
                         "<a class='button is-link is-outlined is-rounded' href='api/paper/delete/"+id+"'> Delete</a>"+"</div> <div class='column'></div> </article> </div></div>");
        });
    }



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
