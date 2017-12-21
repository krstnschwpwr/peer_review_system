var bla = [];

$(document).ready(function () {
    var userid = $('#userid').text();
    loadPapers(userid);


    function useReturnData(data) {
        myvar = data.papers;
        var url = '';
        var id = '';
        $.each(myvar, function (key, paper) {
            id = paper.id;
            $('.mypapers ').append("<div class='columns'><div class='column'><div class='box'> <article class='media'> "+
                "<div class='media-content clearfix'> <div class='content'> <small class='tag is-warning'>" + paper.status + "</small>"+
                                "<h4 class='subtitle is-5'>" + paper.title+ " </h4><br>" + paper.abstract + "</p> </div>"+
                            "<div class='column is-narrow'></div> <a  class='button button is-link is-rounded' href='api/paper/"+id+"'>Show</a>"+
                         "<a class='button is-link is-outlined is-rounded' href='api/paper/delete/"+id+"'> Delete</a>"+"</div> <div class='column'></div> </article> </div></div></div>");
        });
    }



    function loadPapers(userid) {
        $.ajax({
            url: '/api/papers/for-user/' + userid,
            method: 'get',
            dataType: 'json',
            success: function (data) {
                useReturnData(data);
                console.log(data);
            }
        })


    }

});
