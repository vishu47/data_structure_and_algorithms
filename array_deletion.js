const arr = [1,65,78,90,8]
const pos = 2

const DeletionFromArray = () => {
    // we will start loop from where we want to remove the element
    for(let i = pos ; i < arr.length ; i++){
        arr[i] = arr[i+1]
    }
    
    // fixed the length to remove last element
    arr.length = arr.length -1 
    
    console.log(arr)
}

const DefaultMethod =  () => {
    arr.splice(pos , 1)
    console.log(arr)
}

// DeletionFromArray()
DefaultMethod()
