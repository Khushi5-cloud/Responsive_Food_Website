


function Amount()
{
    let n=document.getElementById("food").value;
    let q=document.getElementById("num").value;
    const items =["pizza","burger","hotdog","muffins"];
    const priceOfOne =[230,120,80,50];
    let sum=0;
    for(let i=0;i<4;i++)
    {
        if(items[i]==n)
        {
            sum+=(q*priceOfOne[i]);
        }
    }
    document.getElementById("ans").innerHTML=sum;
    return true;
}