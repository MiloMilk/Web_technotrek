$(document).ready(

    function() {

        $('.comments').each(function () {
                $(this).load($(this).data('url'));
        });

        window.setInterval( function () {
            $('.comments').each(function () {
                $(this).load($(this).data('url'));
            })},
            2000
        );

        function csrfSafeMethod(method) {
            // these HTTP methods do not require CSRF protection
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }

        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", $('meta[name=csrf]').attr("content"));
                }
            }
        });

        //$.ajax({url: $('button.like').data('url')}).done(function(data, status, response) {$('span.likecounter').html(data)});

        $(document).on('click', 'button.putcomment', function () {
            var data = $(this).data();
            $.post(data.url);
        });



        $(document).on('click', 'button.like', function () {
            var data = $(this).data();
            $.post(data.url);
        });


    }



)