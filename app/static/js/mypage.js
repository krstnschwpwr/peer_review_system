var bla = [];

$(document).ready(function () {
    var userid = $('#userid').text();
    loadPapers(userid);


    function useReturnData(data) {
        myvar = data.papers;
        var url = '';
        var id = '';
        var tag;
        $.each(myvar, function (key, paper) {
            id = paper.id;
            if (paper.status === "Accepted") {
                tag = "<small class='tag is-success'>" + paper.status + "</small>"
            } else if (paper.status === "Rejected") {
                tag = "<small class='tag is-danger'>" + paper.status + "</small>"
            } else {
                tag = "<small class='tag is-warning'>" + paper.status + "</small>"
            }
            if (key % 2 === 0) {
                $('.mypapers ').append("<div class='columns mypapercolumn' '><div class='column'><div class='box'> <article class='media'> "+
                "<div class='media-content clearfix'> <div class='content'> "+ tag +
                                "<br><h4 class='subtitle is-5'>" + paper.title+ " </h4><br>" + paper.abstract + "</p> </div>"+
                            "<div class='column is-narrow'></div> <a  class='button button is-link is-rounded' href='api/paper/"+id+"'>Show</a>"+
                         "<a class='button is-link is-outlined is-rounded' href='api/paper/delete/"+id+"'> Delete</a>"+"</div></article> </div></div>");
            } else {
                $('.mypapercolumn ').append("<div class='column'><div class='box'> <article class='media'> "+
                "<div class='media-content clearfix'> <div class='content'> "+ tag +
                                "<br><h4 class='subtitle is-5'>" + paper.title+ " </h4><br>" + paper.abstract + "</p> </div>"+
                            "<div class='column is-narrow'></div> <a  class='button button is-link is-rounded' href='api/paper/"+id+"'>Show</a>"+
                         "<a class='button is-link is-outlined is-rounded' href='api/paper/delete/"+id+"'> Delete</a>"+"</div> <div class='column'></div> </article> </div></div></div>");
            }

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
