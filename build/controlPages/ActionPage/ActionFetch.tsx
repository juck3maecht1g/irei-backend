import React from "react"
import { useState } from "react"
import { passDataDirect, post, passDataAsMap, convertBackToFrontMapping, convertFrontToBackMapping, passDataForActionMapping, passDatalenght, passDataCoordinates, post2 } from "../../backendComunication/BasicOpperations"

const fetchAdressAllActionLists = "http://127.0.0.1:5000/api/get-action_lists"
const postAdressActionList = "http://127.0.0.1:5000/api/set_action_list"
const fetchAdressContentActiveList = "http://127.0.0.1:5000/api/get_action_list_content"
const postAdressAppendAction = "http://127.0.0.1:5000/api/append_action"
const postAdressDeleteAction = "http://127.0.0.1:5000/api/delete_action"
const postAdressSwapActions = "http://127.0.0.1:5000/api/swap_action"
const postAdressCreateActionList = "http://127.0.0.1:5000/api/create_action_list"
const postAdressExecuteList = "http://127.0.0.1:5000/api/executeList"
const postAdressCoordinateType = "http://127.0.0.1:5000/api/set_coordinate_type"
const fetchAdressPositionList = "http://127.0.0.1:5000/api/get_coordinates"
const fetchAdressMapping = "http://127.0.0.1:5000/api/get_mapping_table"
const postAdressMapping = "http://127.0.0.1:5000/api/set_mapping_in_table"
const postAdressMappingPosition= "http://127.0.0.1:5000/api/set_mapping_pos"
const postAdressButtonIndex= "http://127.0.0.1:5000/api/set_button_index"
const fetchAdressALBContent = "http://127.0.0.1:5000/api/get_action_list_button_content"
const fetchAdressCoordinates = "http://127.0.0.1:5000/api/get_coordinates"

/**gets a list of dictionarrys containing a "name" of the action list and a "key"
 * specifieing if sequential or parallel
 * 
 * @param setLists 
 */
export async function GetActionListNames(setLists){ // returns string list
    var [fetched, setfetched] = useState(false) 
    passDataDirect(setLists, fetched, setfetched, fetchAdressAllActionLists)


}
/**
 *  fetches an array of dictionarrys each containing all data nessesary if key != action_list
 *  otherwise containig just the name of the underling actionList and information if it is a paralell od sequential list
 * @param setContent the method to set with the fetched data
 */

export async function GetActionListContent(setContent){ // returns string list
    var [fetched, setfetched] = useState(false)                                     
    passDataDirect(setContent, fetched, setfetched, fetchAdressContentActiveList)


}

/** action is a dictionarry containing the key which action to append, and all nessesary arguments for that action
 */
export async function appendAction( errorfunction, action, setErrorMessage){
    var toPost =  action
    toPost.set("marker", "append_action")
    const result = Object.fromEntries(toPost)
    var reload = false
   
    await post2(result, postAdressAppendAction).then(res => {
        if(res !== "Done") {
            setErrorMessage(res)
            errorfunction()
           reload = false
        }
      else {
       reload = true
      }
    })

    return reload

}


/** informs the backend that the actionlist with the given name was chosen
 * and gets its content
 * 
 * @param setContent 
 * @param name 
 */
export async function SetActionList( errorfunction, action, setErrorMessage){
    console.log(action)
    var toPost =  new Map()
    toPost.set("marker", "set_action_list")
    toPost.set("name", action)
    const result = Object.fromEntries(toPost)
    var reload = false
    await post(result, postAdressActionList).then(res => {
        if(res !== "Done") {
            setErrorMessage(res)
            errorfunction()
           reload = false
        }
      else {
       reload = true
      }
    })

    return reload

}

/** delets the action in the currently changed list at the given position
 * and gets the changed list
 * 
 * @param setContent 
 * @param position 
 */
export async function DeleteAction( errorfunction,position, setErrorMessage){
    var toPost =  new Map()
    toPost.set("marker", "delete_action")
    toPost.set("position", position)
    const result = Object.fromEntries(toPost)
    var reload = false
    await post(result, postAdressDeleteAction).then(res => {
        if(res !== "Done") {
            setErrorMessage(res)
           errorfunction()
           reload = false
        }
      else {
       reload = true
      }
    })

    return reload


}

/** swaps the actions at the two specified positions and gets the modified list
 * 
 * @param setContent 
 * @param first position as int
 * @param second 
 */
export async function SwapActions(first, second,  errorfunction,setErrorMessage){
    var toPost =  new Map()
    toPost.set("marker", "swap")
    toPost.set("first", first)
    toPost.set("second", second)
    const result = Object.fromEntries(toPost)
    var reload = false
    await post(result, postAdressSwapActions).then(res => {
        if(res !== "Done") {
            setErrorMessage(res)
            errorfunction()
           reload = false
        }
      else {
       reload = true
      }
    })

    return reload

}
/** creates a new action listwith given name and given type("sequential_list" or"parallel_list")
 *  and gets the content of the new list
 * @param setContent 
 * @param name 
 * @param type 
 */
export async function CreatetActionList(name:String, type:String,  errorfunction,setErrorMessage){
    var message =  new Map()
    message.set("marker", "create_action_list")
    message.set("name", name)
    message.set("key", type)
    const result = Object.fromEntries(message)
    var reload = false
    await post(result, postAdressCreateActionList).then(res => {
        if(res !== "Done") {
            setErrorMessage(res)
            errorfunction()
           reload = false
        }
      else {
       reload = true
      }
    })

    return reload

}
/** executes the action list with the given name
 * 
 * @param name 
 */
export async function ExecuteActionList(name:String,  errorfunction,setErrorMessage){
    var message =  new Map()
    message.set("marker", "execute_action_list")
    message.set("name", name)
    const result = Object.fromEntries(message)
    var reload = false
    await post(result, postAdressExecuteList).then(res => {
        if(res !== "Done") {
            console.log(res)
            setErrorMessage(res)
            errorfunction()
           reload = false
        }
      else {
       reload = true
      }
    })

    return reload


}

/** sets the type the coordinates are handeled ans displaied in ton the specified type("cartesian","joint")
 * 
 * @param type 
 */
export async function SetCoordinateType(type:String,  errorfunction,setErrorMessage){
    var message =  new Map()
    message.set("marker", "set_coordinate_type")
    message.set("type", type)
    const result = Object.fromEntries(message)
    var reload = false
    await post(result, postAdressCoordinateType).then(res => {
        if(res !== "Done") {
            setErrorMessage(res)
            errorfunction()
           reload = false
        }
      else {
       reload = true
      }
    })

    return reload


}

/** gets all available positions as dict with ("name", and the coordinate "coordinate")
 * 
 * @param setPositions 
 */
export async function GetPositions(setPositions){ // returns Map list
    var [fetched, setfetched] = useState(false) 
    passDataDirect(setPositions, fetched, setfetched, fetchAdressPositionList)


}

/** todo matching naming
 * 
 * @param setMapping 
 */
export async function GetMapping(setMapping){ // returns Map list
    var [fetched, setfetched] = useState(false) 
    await passDataForActionMapping(setMapping, fetched, setfetched, fetchAdressMapping)
}




export async function SetMappingPos(pos:[],  errorfunction,setErrorMessage){
    var reload = false
    await post(pos, postAdressMappingPosition).then(res => {
        if(res !== "Done") {
            setErrorMessage(res)
            errorfunction()
           reload = false
        }
      else {
       reload = true
      }
    })

    return reload


}

export async function SetMapping(mappingRobots,  errorfunction,setErrorMessage){
    mappingRobots = convertFrontToBackMapping(mappingRobots)
    var message = Array()
    for (var x = 0; x<mappingRobots.length; x++) {
        const temp = Object.fromEntries(mappingRobots[x])
        message.push(temp)

    }
    var reload = false
    await post(message, postAdressMapping).then(res => {
        if(res !== "Done") {
            setErrorMessage(res)
            errorfunction()
           reload = false
        }
      else {
       reload = true
      }
    })

    return reload


}


export async function SetButtonIndex(index,  errorfunction,setErrorMessage){
    var reload = false
    console.log("idex", index)
    await post(index, postAdressButtonIndex).then(res => {
        if(res !== "Done") {
            setErrorMessage(res)
            errorfunction()
           reload = false
        }
      else {
       reload = true
      }
    })

    return reload


}



export { convertBackToFrontMapping }

export async function GetALButtonContentLen(setButton) {
    var [fetched, setfetched] = useState(false) 
    await passDatalenght(setButton, fetched, setfetched, fetchAdressALBContent)
}

export async function GetALButtonContent(setButton) {
    var [fetched, setfetched] = useState(false) 
    await passDataDirect(setButton, fetched, setfetched, fetchAdressALBContent)
}



export async function GetCoordinates(setCoordinates){ // returns Map list
    var [fetched, setfetched] = useState(false) 
    await passDataCoordinates(setCoordinates, fetched, setfetched, fetchAdressCoordinates)
}


