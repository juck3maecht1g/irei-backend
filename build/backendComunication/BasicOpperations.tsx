import React from "react"


export async function passDataDirect(set, fetched, setfetched, adress){

    if(fetched) {
        return
        }
        setfetched (true)
        const data = await (
            await fetch(
            adress
            )
        ).json().then(data => {
            console.log("data", data)
            set(data)
        }
        )
}

export async function passDataAsMap(set, fetched, setfetched, adress){

    if(fetched) {
        return
        }
        setfetched (true)
        const data = await (
            await fetch(
            adress
            )
        ).json().then(data => {
            var dir = new Map(Object.entries(data))
            set(dir)
        }
        )
}


export async function post (content, postAdress){

    const response = await fetch(postAdress, {
        'method': 'POST',
        headers : {
        'Content-Type': 'application/json'
        },
        body : JSON.stringify(content)
    })
   
    return (await response.text()).toString()

}  


export async function post2 (content, postAdress){
    console.log("COntent", content)
    console.log( JSON.stringify(content))
    console.log("ADTRESS", postAdress)
        console.log("ves")

    var response = await fetch(postAdress, {
        'method': 'POST',
        headers : {
        'Content-Type': 'application/json'
        },
        body : JSON.stringify(content)
    })
    response = await response
    return await (await (await response.text()).toString())

}  



export async function passDataForActionMapping(set, fetched, setfetched, adress){

    if(fetched) {
        return
        }
        setfetched (true)
        const data = await (
            await fetch(
            adress
            )
        ).json().then(data => {
            console.log(data)
            set(convertBackToFrontMapping(data))
        }
        )
}



export function convertFrontToBackMapping(frontMapping) {
    var list = Array()
    for (var x = 0; x< frontMapping.length; x++) {
        var elem = frontMapping[x]
        var temp = new Map() 
        var name = elem.get("name")
        temp.set(name.split(".")[0], elem.get("robot"))
        list.push(temp)
    }
    return list

}

export function convertBackToFrontMapping(backMapping) {
    var list = Array()
   
    var totalMap = new Map(Object.entries(backMapping))
    for (let key of totalMap.keys()) {
        var elem = new Map()
        elem.set("name", key + ". robot in this list")
        elem.set("robot", totalMap.get(key))
        list.push(elem)
    } 
    return list

}

export async function passDatalenght(set, fetched, setfetched, adress){

    if(fetched) {
        return
        }
        setfetched (true)
        const data = await (
            await fetch(
            adress
            )
        ).json().then(data => {
            console.log("data", data)
            set(data.length)
        }
        )
}


export async function passDataCoordinates(set, fetched, setfetched, adress){

    if(fetched) {
        return
        }
        setfetched (true)
        const data = await (
            await fetch(
            adress
            )
        ).json().then(data => {
            console.log("dataCoord", data)
            var toReturn = new Array()
            for(var elem of data) {
                console.log(elem)
                toReturn.push(new Map(Object.entries(elem)))
            }
            console.log("return", toReturn)
            set(toReturn)
        }
        )
}



export async function passDataMatches(set,reference, fetched, setfetched, adress){

    if(fetched) {
        return
        }
        setfetched (true)
        const data = await (
            await fetch(
            adress
            )
        ).json().then(data => {
           if(data == reference){
            set(true)
           }else {
            set(false)
           }
        }
        )
}