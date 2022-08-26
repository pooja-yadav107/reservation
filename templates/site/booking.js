var tickets = [
    {
        no:1, amount:100
    },
    {
        no:2, amount:200
    },
    {
        no:3, amount:300
    },
    {
        no:4, amount:400
    },
    {
        no:5, amount:500
    },
    {
        no:6, amount:600
    },
    {
        no:7, amount:700
    },
    {
        no:8, amount:800
    },
    {
        no:9, amount:900
    },
    {
        no:10, amount:1000
    }
];
str = ``;
tickets.forEach(function(value, index){
    // console.log(value, index)
    str = str + `<div class='col-xl-1' for='${value.no}#${value.amount}' onclick='myfun(this)'>${value.no} <br/> ${value.amount}</div>`

})
// console.log(str)
document.getElementById("maindiv").innerHTML = str;

arr1 = [];
arr2 = [];
function myfun(myvar){
    // console.log(myvar)
    let ans = myvar.attributes.for.value;
    // console.log(ans)
    let ans1 = ans.split('#')
    let position = arr1.indexOf(ans1[0]);

    if(position == -1){
        arr1.push(ans1[0]);
        arr2.push(ans1[1]);
        msg = "Tickets Added"
    }
    else{
        msg = "Ticket Already Exits"
    }
    document.getElementById("msg").innerHTML = msg;
    final_no = arr1.join(",")
    document.getElementById("no").innerHTML = final_no;

    final_amount = arr2.join('+');
    // console.log(final_amount)
    
    total_amount = eval(final_amount);
    // console.log(total_amount)
    document.getElementById("amount").innerHTML = total_amount;
    myvar.style.background = "#f00";
    
}