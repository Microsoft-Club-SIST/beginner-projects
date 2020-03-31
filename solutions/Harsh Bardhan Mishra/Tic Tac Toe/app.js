let currentPlayer = "X",
    playAs = "X",
    isMulti = false,
    gameInProgress = false,
    settingsEnabled = true,
    gameOver = false

//select the DOM elements we need
let gameMessageDOM = document.getElementsByTagName("message")[0],
    btnResetDOM = document.getElementsByTagName("btn-reset")[0],
    optionPlayAsDOM = document.getElementsByTagName("switch-box")[0],
    optionModeDOM = document.getElementsByTagName("switch-box")[1],
    switchPlayAsDOM = document.getElementsByTagName("switch")[0],
    switchModeDOM = document.getElementsByTagName("switch")[1],
    positionsDOM = document.getElementsByTagName("game-position")

//setup gameBoard array from positions elements
let gameBoard = [new Array(3),new Array(3),new Array(3)]
for(let position of positionsDOM){
  position.x = +position.getAttribute("x")
  position.y = +position.getAttribute("y")
  position.empty = true
  position.addMark = function(str){
    if(this.empty && str == "X" || str == "O"){
      this.innerHTML = str
      this.empty = false
    }
  }
  position.removeMark = function(){
    this.innerHTML = ""
    this.empty = true
  }
  position.addEventListener("click", handlePositionClick, false)
  gameBoard[position.x][position.y] = position
}

btnResetDOM.addEventListener("click", resetGame, false)
optionPlayAsDOM.addEventListener("click", setPlayAs, false)
optionModeDOM.addEventListener("click", setMode, false)

function handlePositionClick(){
  let gameState
  if(!gameInProgress){
    currentPlayer = playAs
    gameInProgress = true
    disableSettings()
  }
  //Human Player
  if(this.empty && !gameOver){
    this.addMark(currentPlayer)
    gameState = checkBoard(this)
    checkGameover(gameState)
    switchPlayer()
  }
  //CPU Player
  if(!isMulti && !gameOver){
    gameState = checkBoard(runCPUturn(gameState))
    checkGameover(gameState)
    switchPlayer()
  }
}

function runCPUturn(gameState){
  //block
  if(gameState.match.length > 0){
    for(let position of gameState.match){
      if(position.empty){
        position.addMark(currentPlayer)
        return position
      }
    }
  }
  //mark center
  if(gameBoard[1][1].empty){
    gameBoard[1][1].addMark(currentPlayer)
    return gameBoard[1][1]
  }
  //mark corners
  for(let x = 0; x < 3; x+=2){
    for(let y = 0; y < 3; y+=2){
      if(!(x == 0 && y == 0) && gameBoard[x][y].empty){
        gameBoard[x][y].addMark(currentPlayer)
        return gameBoard[x][y]
      }
    }
  }
  //mark others
  for(let x = 0; x < 3; x++){
    for(let y = 0; y < 3; y++){
      if(!(x == 0 && y == 0) && gameBoard[x][y].empty){
        gameBoard[x][y].addMark(currentPlayer)
        return gameBoard[x][y]
      }
    }
  }
}

function switchPlayer(){
  currentPlayer = currentPlayer == "X" ? "O" : "X"
  gameMessageDOM.innerHTML = currentPlayer + "'s Turn"
}

function resetGame(){
  gameMessageDOM.innerHTML = playAs + "'s Turn"
  gameMessageDOM.style.display = "flex"
  btnResetDOM.style.display = "none"
  for(let position of positionsDOM){
    position.removeMark()
    position.setAttribute("class", "")
  }
  gameInProgress = false
  enableSettings()
  gameOver = false
}

function checkGameover(gameState){
  let isTie = gameBoard.every((x)=>x.every((position)=>!position.empty))
  if(gameState.isWin || isTie){
    gameMessageDOM.style.display = "none"
    btnResetDOM.style.display = "block"
    gameOver = true
    for(let shouldFade of positionsDOM){
      if((isTie && !gameState.isWin) || !gameState.match.includes(shouldFade)){
        shouldFade.setAttribute("class", "darken")
      }
    }
  }
}

function setPlayAs(){
  if(settingsEnabled){
    if(playAs == "X"){
      playAs = "O"
      switchPlayAsDOM.style.transform = "translateX(10px)"
    }
    else{
      playAs = "X"
      switchPlayAsDOM.style.transform = "translateX(-10px)"
    }
    gameMessageDOM.innerHTML = playAs + "'s TURN"
  }
}

function setMode(){
  if(settingsEnabled){
    if(!isMulti){
      isMulti = true
      switchModeDOM.style.transform = "translateX(10px)"
    }
    else{
      isMulti = false
      switchModeDOM.style.transform = "translateX(-10px)"
    }
  }
}

function disableSettings(){
  settingsEnabled = false
  switchPlayAsDOM.style.background = '#555'
  switchModeDOM.style.background = '#555'
}

function enableSettings(){
  settingsEnabled = true
  switchPlayAsDOM.style.background = '#000'
  switchModeDOM.style.background = '#000'
}

//checks the board for win conditions 
//or possible future win conditions (to be used by CPU Player) 
//based on the last mark added to board
function checkBoard(curr){
  let result = {
    isWin: false,
    match: []
  }
  for(let dx = -1; dx < 2; dx++){
    for(let dy = -1; dy < 2; dy++){
      if(!(dx == 0 && dy == 0)){
        if((curr.x+dx < 3 && curr.x+dx > -1 && curr.y+dy < 3 && curr.y+dy > -1) 
        && gameBoard[curr.x+dx][curr.y+dy].innerHTML == curr.innerHTML){
          if((curr.x+dx*2 < 3 && curr.x+dx*2 > -1 && curr.y+dy*2 < 3 && curr.y+dy*2 > -1)){
            result.match.push(curr,gameBoard[curr.x+dx][curr.y+dy],gameBoard[curr.x+dx*2][curr.y+dy*2])
            if(gameBoard[curr.x+dx*2][curr.y+dy*2].innerHTML == curr.innerHTML){
              return {isWin: true, match: [curr,gameBoard[curr.x+dx][curr.y+dy],gameBoard[curr.x+dx*2][curr.y+dy*2]]}
            }
          }
          if((curr.x+dx*-1 < 3 && curr.x+dx*-1 > -1 && curr.y+dy*-1 < 3 && curr.y+dy*-1 > -1)){
            result.match.push(curr,gameBoard[curr.x+dx][curr.y+dy],gameBoard[curr.x+dx*-1][curr.y+dy*-1])
            if(gameBoard[curr.x+dx*-1][curr.y+dy*-1].innerHTML == curr.innerHTML){
              return {isWin: true, match: [curr,gameBoard[curr.x+dx][curr.y+dy],gameBoard[curr.x+dx*-1][curr.y+dy*-1]]}
            }
          }
        }
        else if((curr.x+dx*2 < 3 && curr.x+dx*2 > -1 && curr.y+dy*2 < 3 && curr.y+dy*2 > -1)
        && gameBoard[curr.x+dx][curr.y+dy].empty
        && gameBoard[curr.x+dx*2][curr.y+dy*2].innerHTML == curr.innerHTML){
          result.match.push(curr,gameBoard[curr.x+dx][curr.y+dy],gameBoard[curr.x+dx*2][curr.y+dy*2])
        }
      }
    }
  }
  return result
}
