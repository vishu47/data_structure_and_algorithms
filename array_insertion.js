const arr = [1,65,78,90,8]
const elem = 87
const position = 3


const InsertionInArray = (arr , elem , position) => {
      console.log(arr, 'old')
    for(let i = arr.length - 1; i >= position ; i--  ){
        arr[i+1] = arr[i]
        if(i === position){
            arr[i] = elem
        }
    }    
    console.log(arr)
}


const SpliceMethod = (arr, elem, position) => {
    arr.splice(position , 0 , elem)
    console.log(arr , 'splice method')
}

// InsertionInArray(arr ,elem,position )
SpliceMethod(arr ,elem,position )
