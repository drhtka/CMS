myposts= document.getElementsByClassName('myPosts')[0];

function postsApi(data){
    alert('1')
    // tesy = '123445'
    // console.log('tesy')
    // console.log(tesy)
    // console.log('123445')
    // console.log(tesy)

    var all_posts = data
    for( i=0; i<all_posts.length; i++ ){
        // fields = ('brand_name', 'model', 'price', 'category')
        api_cicl += '<div class="col-6 col-sm-5 col-md-4 col-lg-3 col-xl-3 child-row">' +
            // '<a class="text-decoration-none" href=' + link + all_posts[i].id + '>' + all_posts[i].brand_name + '</a>' +
            '<div class="blog_id">' + '<span>Номер поста: </span>' + all_posts[i].id + '</div>' +
            // '<div>' +'<img class="main_img" src="' + all_posts[i].photo + '"/>' + '</div>' +
            // '<div class="blog_text col-12 col-sm-12 col-md-12 col-lg-12 col-xl-12 text-truncate">' + all_posts[i].text + '</div>' +
            //'<div class="author">' + all_posts[i].author + '</div>' +
            '<div class="publish_date">' + all_posts[i].model_name + '</div>' +
            '</div>'
    }
    console.log(myposts)
    myposts.innerHTML = myposts.innerHTML + api_cicl
    console.log(myposts.innerHTML)
}


window.onload = postsApi

fetch('http://127.0.0.1:8250/api/posts/')
    // Handle success
    .then(response => response.json())  // convert to json
    .then(data => console.log(data))
     console.log('data')
    // .then(data => this.postsApi(data))
