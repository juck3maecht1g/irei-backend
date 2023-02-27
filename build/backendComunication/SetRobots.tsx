import React from "react"
import { post } from "./BasicOpperations"

const postAdressExpRobots = "http://127.0.0.1:5000/api/setRobotsExp"
const postAdressChangeGripperRobots= "http://127.0.0.1:5000/api/setRobotsGripper"
const postAdressSavePositionRobots = "http://127.0.0.1:5000/api/setSavePosition"



export async function SetExpRobots(action, robots, setErrorMessage){
    var ipList = [""]
    for(var key of robots.keys()){
      ipList.push(key)
    }
    var message =  new Map()
    message.set("marker", "SetExpRobots")
    message.set("robot_ips", ipList)
    var reload = false
    const result = Object.fromEntries(message)
    await post(result, postAdressExpRobots).then(res => {
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
export async function SetChangeGripperRobots(action, robots, setErrorMessage){
  var ipList = [""]
    for(var key of robots.keys()){
      ipList.push(key)
    }
    var message =  new Map()
    message.set("marker", "SetChangeGripperRobots")
    message.set("robot_ips", ipList)
    var reload = false
    const result = Object.fromEntries(message)
    await post(result, postAdressChangeGripperRobots).then(res => {
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
export async function SetSavePositionRobot(action, robots, setErrorMessage){
  var ipList = Array()
  
      ipList.push(robots)
    
    
    var message =  new Map()
    message.set("marker", "SetSavePositionRobots")
    message.set("robot_ip", ipList)
    var reload = false
    const result = Object.fromEntries(message)
    await post(result, postAdressSavePositionRobots).then(res => {
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



