const arr = [1,65,78,976,63,5,2532,57,658,65,8] 
const Traversing1 = () => {
    for (let elem of arr) {
        console.log(elem)
    }
}

const Traversing2 = () => {
    for (let elem = 0;elem < arr.length ; elem++) {
        console.log(arr[elem])
    }
}


Traversing2(arr)
