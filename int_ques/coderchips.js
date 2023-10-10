const arr1 = [-10,65,22,333,8]
const arr2 = [-11,22,13,54,98]
const arr3 = []


const DefaultMergingMethodMethod = () => {
  const  an = [...arr1,...arr2]
    for (let i = 0; i < an.length; i++) {
      if(!arr3[i].includes(an[i])){
        arr3[i] = an[i]
      }
    }
  console.log(arr3,'kkk')
}


DefaultMergingMethodMethod()