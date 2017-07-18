function appendToWidget(a, b, c, d) {
    a = document.querySelector(a);
    b = document.createElement(b);
    b.innerHTML = d;
    b.className += c;
    a.appendChild(b)
}
function getJSON(a, b) {
    var c = new XMLHttpRequest;
    c.open("GET", a, !0);
    c.onload = function() {
        if (200 === c.status) {
            var a = JSON.parse(c.responseText);
            b(a)
        }
    };
    c.send()
}
function ready(a) {
    "loading" != document.readyState ? a() : document.addEventListener("DOMContentLoaded", a)
}
function start() {
    appendToWidget("body", "style", "", "@import url(https://fonts.googleapis.com/css?family=Noto+Sans:400,700);.gh-widget-link,.gh-widget-link:hover{text-decoration:none}.gh-widget-container{display:flex;flex-direction:row;flex-wrap:no-wrap;align-items:center;justify-content:center;color:#333;font-family:'Noto Sans',sans-serif}.gh-widget-personal-details .bio{color:#222222l;} .gh-widget-stats .count{color:#4078C0}.github-widget{border:1px solid #DDD;max-width:350px}.gh-widget-item{flex:1;text-align:center;padding:10px}.gh-widget-repositories .language{text-align:left}.gh-widget-repositories .language div,.gh-widget-repositories .stars div{padding:5px 0}.gh-widget-photo{flex:2}.gh-widget-photo img{border-radius:100%;max-width:80px}.gh-widget-personal-details{flex:6}.gh-widget-personal-details .full-name{font-size:1.5em;line-height:1.5em}.gh-widget-personal-details .location{font-size:.8em}.gh-widget-stats .count{font-size:1.2em;font-weight:700}.gh-widget-repositories .names{flex:2;text-align:left}.gh-widget-repositories .names div{padding:5px 0;text-overflow:ellipsis}.gh-widget-follow{flex:2}.gh-widget-active-time{flex:4;font-size:.8em}.gh-widget-heading{font-weight:400;color:#666}.gh-widget-hr{border:1px solid #DDD}.gh-widget-link{color:#4078C0}.gh-widget-follow button{width:100%;height:2em;border:none;background:#ddd} img{ vertical-align:middle;} .github-box-title{position:relative;border-bottom:1px solid #DDD;border-radius:3px 3px 0 0;background:#FCFCFC;background:-moz-linear-gradient(#FCFCFC,#EBEBEB);background:-webkit-linear-gradient(#FCFCFC,#EBEBEB);}");
    for (var a = document.querySelectorAll(".github-widget"), b = 0; b < a.length; b++) {
        var c = a[b];
        c.setAttribute("id", "widget" + b);
        appendToWidget("#widget" + b, "div", "", '<div class="gh-widget-container"><div class="gh-widget-item gh-widget-photo"></div><div class="gh-widget-item gh-widget-personal-details"></div></div><div class="gh-widget-container gh-widget-stats"></div><hr class="gh-widget-hr"><div class="gh-widget-container"><div class="gh-widget-item gh-widget-heading">Popular Repositories</div></div><div class="gh-widget-repositories"></div><div class="gh-widget-container"><div class="gh-widget-item gh-widget-follow"></div><div class="gh-widget-item gh-widget-active-time"></div></div>');
        c = c.dataset.username;
        fetchRepos(c, "#widget" + b);
        fetchUserDetails(c, "#widget" + b)
    }
}
ready(start);
function fetchRepos(a, b) {
    getJSON("https://api.github.com/users/" + a + "/repos",
    function(a) {
        updateRepoDetails(topRepos(a), b);
        updateLastPush(lastPushedDay(a), b)
    })
}
function fetchUserDetails(a, b) {
    getJSON("https://api.github.com/users/" + a,
    function(a) {
        updateUserDetails(a, b)
    })
}
function updateLastPush(a, b) {
    appendToWidget(b + " .gh-widget-active-time", "span", "", "Last active: " + (a ? a + " day(s) ago": "Today"))
}
function lastPushedDay(a) {
    for (var b = new Date,
    c, d = 9999999999999,
    e = 0; e < a.length; e++) {
        var f = new Date(a[e].pushed_at);
        b - f < d && (c = f, d = b - f)
    }
    return Math.floor((b - c) / 864E5)
}
function updateUserDetails(a, b) {
    appendToWidget(b + " .gh-widget-personal-details", "div", "full-name", '<a class="gh-widget-link" target="new" href="' + a.html_url + '">'+a.name+'</a>');
    a.bio && appendToWidget(b + " .gh-widget-personal-details", "div", "bio", a.bio);
    a.location && appendToWidget(b + " .gh-widget-personal-details", "div", "location", '<img src="http://www.iconres.com/android/res/material_icons/external-assets/v4/icons/png/ic_location_on_black_48dp.png" width=20 height=20 />'+a.location);
	a.email && appendToWidget(b + " .gh-widget-personal-details", "div", "email", '<img src="http://www.iconres.com/android/res/material_icons/external-assets/v4/icons/png/ic_email_black_48dp.png" width=20 height=20 />'+a.email);
    appendToWidget(b + " .gh-widget-stats", "div", "gh-widget-item", '<div class="count"><a class="gh-widget-link" target="new" href="' + a.html_url + '/followers">' + a.followers + '</a></div><div class="stat-name">Followers</div>');
    appendToWidget(b + " .gh-widget-stats", "div", "gh-widget-item", '<div class="count"><a class="gh-widget-link" target="new" href="' + a.html_url + '/following">' + a.following + '</a></div><div class="stat-name">Following</div>');
    appendToWidget(b + " .gh-widget-stats", "div", "gh-widget-item", '<div class="count"><a class="gh-widget-link" target="new" href="' + a.html_url + '/?tab=repositories">' + a.public_repos + '</a></div><div class="stat-name">Repositories</div>');
    appendToWidget(b + " .gh-widget-photo", "span", "", '<img src="' + a.avatar_url + '">');
    appendToWidget(b + " .gh-widget-follow", "button", "", '<a class="gh-widget-link" target="new" href="' + a.html_url + '">Home</a>')
}
function updateRepoDetails(a, b) {
    for (var c = 0; c < a.length; c++) 
		appendToWidget(b + " .gh-widget-repositories", "div", "gh-widget-container", '<div class="gh-widget-item names"><div><a class="gh-widget-link" href="' + a[c].repoUrl + '">' + a[c].name + '</a></div></div><div class="gh-widget-item language"><div>' + (a[c].language ? a[c].language: "Unknown") + '</div></div><div class="gh-widget-item stars"><div>&#9733;' + a[c].stars + "</div></div>")
}
function topRepos(a) {
    a.sort(function(a, b) {
        return a.stargazers_count === b.stargazers_count ? 0 : a.stargazers_count > b.stargazers_count ? -1 : 1
    });
    a = a.slice(0, 3);
    var b = [],
    c;
    for (c in a) {
        var d = a[c];
        b.push({
            name: d.name,
            stars: d.stargazers_count,
            language: d.language,
            repoUrl: d.html_url
        })
    }
    return b
};