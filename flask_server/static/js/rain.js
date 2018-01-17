/**
 * Created by rainp1ng on 4/18/16.
 */

var $$=document;

var current_ip=$$.getElementById("ip");
if(current_ip!=null){
    if(current_ip.value=="")
        current_ip.value=window.location.href;
}

var search_btn = $$.getElementById("search_btn");
var search_question = $$.getElementById('search_question');
var tip = $$.getElementById('search_tip');
var result_grid = $$.getElementById('display_grid');
var result_list = $$.getElementById('search_result_list');


if(search_btn!=null){
search_btn.onclick = function () {
    var question = search_question.value;
    if(question=='')
        return
    tip.innerHTML = '搜索中...';
    tip.style.display = '';
    url = '/search/' + question;
    result = request('get', url);
    json_result = jQuery.parseJSON(result);
    if(json_result['stat'] == '200'){
        tip.style.display = 'none';
        show_result(json_result['result']);
    }else{
        tip.innerHTML = '网络异常或暂无推荐结果,请重试!';
        result_grid.style.display = 'none';
    }
};
}


function show_result(json_result){
    result_grid.style.display = '';
    result = ''
    for(i in json_result){
        result += '<tr><td><a href="' + json_result[i]['link'] + '">' + json_result[i]['website'] + '</a></td><td>' + json_result[i]['type'] + '</td><td>' + json_result[i]['score'] + '</td></tr>';
    }
    result_list.innerHTML = result;
};


function request(action,url,data){
    var request=new XMLHttpRequest();
    if(action=="post"){
        request.open('POST',url,false);
        request.send(data);
        //alert(request.responseText);
        return request.responseText;
    }else{
        request.open('GET',url,false);
        request.send();
        //alert(request.responseText);
        return request.responseText;
    }
};
