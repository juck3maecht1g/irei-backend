import React from "react"
import { useState } from "react"
import { post, passDataAsMap, passDataDirect, passDataMatches } from "./BasicOpperations"
const fetchAdressGetExperiments = "http://127.0.0.1:5000/api/getRegExp"
const postAdressChosenExperiment = "http://127.0.0.1:5000/api/setup_exp"
const fetchAdressGetDirectories = "http://127.0.0.1:5000/api/get_content"
const postAdressNavigateUP = "http://127.0.0.1:5000/api/navigate_up"
const postAdressNavigateDown = "http://127.0.0.1:5000/api/navigate_down"
const postAdressCreateDirectory = "http://127.0.0.1:5000/api/create_dirctory"
const postAdressDeleteDirectory = "http://127.0.0.1:5000/api/delete_dirctory"
const postAdressConfirmDirChoisey = "http://127.0.0.1:5000/api/confirm_dir_coise"
const fetchAdressName = "http://127.0.0.1:5000/api/get_base_name_dir"
const fetchAdressPath = "http://127.0.0.1:5000/api/file_name"
const fetchAdressTop = "http://127.0.0.1:5000/api/is_top"

// contains dummy

/** gets names of all registered experiments as array
 * 
 */
export async function GetExperiments(setExperiments){
    var [fetched, setfetched] = useState(false) 
    passDataDirect(setExperiments, fetched, setfetched, fetchAdressGetExperiments)


}

export async function SetExperiment(action, name, setErrorMessage){
    var message =  new Map()
    message.set("marker", "SetExperiment")
    message.set("experiment", name)
    const result = Object.fromEntries(message)
    var reload = false
    await post(result, postAdressChosenExperiment).then(res => {
        if(res !== "Done") {
            setErrorMessage(res)
            action()
           reload = false
        }
      else {
       reload = true
      }
    })

    return reload

}

// contains dummy

/** gets a dictionary with two entrys
 * "to_navigate" all child experiments
 * "cant_navigate" all other files in directory
 * @param setDirectories 
 */
export async function GetDirectories(setDirectories){
    var [fetched, setfetched] = useState(false) 
   passDataAsMap(setDirectories, fetched, setfetched, fetchAdressGetDirectories)
    

    
}

export async function GetPath(setPath){
    var [fetched, setfetched] = useState(false) 
   passDataDirect(setPath, fetched, setfetched, fetchAdressPath)
    

    
}


const markerNavUP = "navigate_up"
export async function NavigateUP(action,setErrorMessage){
    var message =  new Map()
    var reload = false
    message.set("marker", markerNavUP)
    const result = Object.fromEntries(message)
    await post(result, postAdressNavigateUP).then(res => {
        if(res !== "Done") {
            setErrorMessage(res)
            action()
           reload = false
        } else {

       reload = true}
    })

    return reload


}
const markerNavDown = "navigate_down"
export async function NavigateDown(action, name, setErrorMessage){
    var message =  new Map()
   
    message.set("marker", markerNavDown)
    message.set("dir", name)
     var reload = false
    const result = Object.fromEntries(message)
    await post(result, postAdressNavigateDown).then(res => {
        if(res !== "Done") {
            setErrorMessage(res)
            action()
           reload = false
        }
      else {
       reload = true
      }
    })

    return reload

}

const markerCreate = "create"
export async function Create(action, name, setErrorMessage){
    var message =  new Map()
    message.set("marker", markerCreate)
    message.set("name", name)
    const result = Object.fromEntries(message)
    var reload = false
    await post(result, postAdressCreateDirectory).then(res => {
        if(res !== "Done") {
            setErrorMessage(res)
            action()
           reload = false
        }
      else {
       reload = true
      }
    })

    return reload

}
const markerDeleteDirectory = "delete_directory"
export async function DeleteDirectory(action, name, setErrorMessage){
    var message =  new Map()
    message.set("marker", markerDeleteDirectory)
    message.set("name", name)
    const result = Object.fromEntries(message)
    var reload = false
    await post(result, postAdressDeleteDirectory).then(res => {
        if(res !== "Done") {
            setErrorMessage(res)
            action()
           reload = false
        }
      else {
       reload = true
      }
    })

    return reload

}

export function BaseNameDir(setName) {
    var [fetched, setFetched] = useState(false) 
    passDataDirect(setName, fetched, setFetched, fetchAdressName)
}

const confirmMarker = "confirm_dir_coise"
export async function confirmDirChoise(action,setErrorMessage) {
    var reload = false
    await post(confirmMarker, postAdressConfirmDirChoisey).then(res => {
        if(res !== "Done") {
            setErrorMessage(res)
            action()
           reload = false
        }
      else {
       reload = true
      }
    })

    return reload

}

export async function IsTop(setTop) {
    var [fetched, setFetched] = useState(false) 
    var reference = "true"
   await passDataMatches(setTop, reference, fetched, setFetched, fetchAdressTop)
}


