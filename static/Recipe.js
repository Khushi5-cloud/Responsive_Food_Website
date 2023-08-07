onload = fetch("./Recipe_data.csv").then(res=>{
    return res.text()
}).then(d=>{
    
   
    let r=d.split("\n") 
    ihtml=""
    for(let i=1;i<11;i++) 
    {
        console.log("[")
        let c=r[i].split(",")
        for(let j=0;j<3;j++)
        {
        console.log(c[j])
        }
        console.log("]")   
        ihtml+=`
        <div class="card">
    <div class="card-body">
      <h4 class="card-title">${c[1]}</h4>
      <p class="card-text">Craving for your next meal, try ${c[1]}.</p>
      <a href="${c[2]}" class="card-link">Recipe link</a>
    </div>
    </div>
        `
        card_big.innerHTML=ihtml

        
    }

})

