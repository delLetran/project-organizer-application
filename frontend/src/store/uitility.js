const updateObject = (obj, update) => {
  return {
    ...obj, ...update
  }
}

// const appendObject = (obj, update, item) => {
//   let update = update
//   return {
//     ...obj, update: [item]
//   }
// }





export default updateObject
export {
  updateObject
}