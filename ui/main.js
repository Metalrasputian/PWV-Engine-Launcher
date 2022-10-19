function openFile(){
    var fileName = pywebview.api.getDir().then(showFile);
}

function showFile(path){
    //var fileText = document.getElementById('filename').innerHTML = path;

    var dEngine = pywebview.api.getDefaultEngine(path).then(function(response){
        document.getElementById('filename').innerHTML = response;
    });
    
}