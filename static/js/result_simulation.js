function validate_team(){
    team1 = document.getElementById("id_team1").value;
    team2 = document.getElementById("id_team2").value;
    runs = document.getElementById("id_number_runs").value;
    if(team1 == team2){
        alert("Cannot Select Same team");
    }
    if(runs == 0){
        alert("Cannot Simulate Zero Runs Match");
    }
    // console.log(team1,team2);
}