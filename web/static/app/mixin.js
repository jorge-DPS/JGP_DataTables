function dictToJSON(dict) {
    if (!!dict) {
        return JSON.parse(dict.replace(/'/g, '"').replace(/None/g, 'null')
            .replace(/False/g, 'false').replace(/True/g, 'true'));
    }
    return null;
}

var csrftoken = Cookies.get('csrftoken');
console.log(csrftoken);

Vue.http.interceptors.push(function(request, next) {
    request.headers.set('X-CSRFToken', csrftoken);
    // request.headers.set('Authorization', 'Bearer TOKEN');
    next();
});