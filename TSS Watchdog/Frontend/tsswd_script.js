window.onload = function() {
	loadNewSuspiciousTweets();
};

function loadNewSuspiciousTweets() {
    var tweetTable = document.getElementById("tweet table");
    var reader = new FileReader();
    reader.readAsText("../Backend/suspicious-tweets.json");
	var suspiciousTweets = JSON.parse(reader);
    console.log(suspiciousTweets)

	for (tweet in suspiciousTweets){
	    console.log(tweet['user'])
        var row = tweetTable.insertRow(0);
        var cell1 = row.insertCell(0);
        var cell2 = row.insertCell(1);
        var cell3 = row.insertCell(2);
        cell1.innerHTML = tweet.user;
        cell2.innerHTML = "Tweet";
        cell3.innerHTML = "Users";
	}
}
