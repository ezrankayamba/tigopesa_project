  (function(){
    tree = document.getElementById('treetable-rows')
    rows = tree.getElementsByTagName('tr')

    for (let row of rows) {
      let id = row.dataset.id
      let level = row.dataset.level
      let hasChildren = row.dataset.hasChildren > 0
      console.log('hasChildren',hasChildren)
      let parentId = row.dataset.parentId
      if(!parentId){
        row.classList.add("root-node");
        row.style.display='table-row'
      }

      if(hasChildren){
        let nameTd = row.querySelector('td.name')
        nameTd.addEventListener('click',(e)=>{
          //oi-caret-right
          //oi-caret-bottom
          let span = row.querySelector('td.name > span')
          if(span.classList.contains('oi-caret-right')){
            span.classList.remove('oi-caret-right')
            span.classList.add('oi-caret-bottom')

            for (let row2 of rows) {
              let id2 = row2.dataset.id
              let parentId2 = row2.dataset.parentId
              if(id === parentId2){
                 row2.style.display='table-row'
              }
            }
          }else{
            span.classList.remove('oi-caret-bottom')
            span.classList.add('oi-caret-right')
            let match = true;
            for (let row2 of rows) {
              let span2 = row2.querySelector('td.name > span')
              let id2 = row2.dataset.id
              let parentId2 = row2.dataset.parentId
              if(id === parentId2){
                 row2.style.display='none'
                 span2.classList.remove('oi-caret-right')
                 span2.classList.add('oi-caret-bottom')
                 match = true
              }
              // console.log(match, row2.dataset.level, level, row2)
              if(match && row2.dataset.level > level){
                 row2.style.display='none'
                 span2.classList.remove('oi-caret-bottom')
                 span2.classList.add('oi-caret-right')
              }else{
                 match = false;
              }
            }
          }
        })
      }else{
        let span = row.querySelector('td.name > span')
        if(span.classList.contains('oi-caret-right')){
          span.classList.remove('oi-caret-right')
          span.classList.add('oi-file')
        }
      }
    }
  })();
