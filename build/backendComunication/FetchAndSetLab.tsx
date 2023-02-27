import React from "react"
import { post } from "./BasicOpperations";

const postAdressLab = "http://127.0.0.1:5000/api/setCurrentLab"
const fetchAdress = "http://127.0.0.1:5000/api/getLab";
 
 
 /**informs the backend which lab was chosen
     * 
     * @param labName  name of the chosen lab
     */
 export async function informLabChoise (action, labName, setErrorMessage){
  var message =  new Map()
  message.set("marker", "setCurrentLab")
  message.set("name", labName)
  var reload = false
  const result = Object.fromEntries(message)
  await post(result, postAdressLab).then(res => {
      if(res !== "Done") {
          setErrorMessage(res)
          action()
          console.log(1)
         reload = false
      }
    else {
     reload = true
    }
  })

  return reload

    
  }

/** gets all labs as dict also containing all robots
 * 
 * 
 * replace testdik with data
 * 
 */
export async function getLabs(setLabs, fetched, setfetched){
  
    if(fetched) {
      return
    }
     setfetched (true)
      const data = await (
        await fetch(
          fetchAdress
        )
      ).json().then(data => {
        var labs = new Map()
        for(let i = 0; i < data.length; i++) {
            var robots = new Map()
            for(let j = 0; j < data[i].robots.length; j++) {
              robots.set(data[i].robots[j].ip, data[i].robots[j].name)
            }
          labs.set(data[i].name, robots)
        }
        setLabs(labs)
      }
      )
     
          // set state when the data received
  }