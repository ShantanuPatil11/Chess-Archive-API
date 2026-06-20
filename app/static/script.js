let board = null;

let game = new Chess();

let moves = [];

let currentMove = 0;

function updateBoard() {

    let tempGame = new Chess();

    for (let i = 0; i < currentMove; i++) {
        tempGame.move(moves[i]);
    }

    board.position(tempGame.fen());

    document.getElementById("moveNumber").innerText =
        currentMove;

    document.getElementById("totalMoves").innerText =
        moves.length;
}

function loadGame() {

    const pgn =
        document.getElementById("pgnInput").value;

    game = new Chess();

    try {

    game.load_pgn(
        pgn,
        {
            newline_char: "\n"
        }
    );

} catch (error) {

    console.error(error);

    alert("Unable to load PGN");

    return;
}

    moves = game.history();

    currentMove = 0;

    board.start();

    updateBoard();
}

function nextMove() {

    if (currentMove < moves.length) {

        currentMove++;

        updateBoard();
    }
}

function previousMove() {

    if (currentMove > 0) {

        currentMove--;

        updateBoard();
    }
}

function firstMove() {

    currentMove = 0;

    updateBoard();
}

function lastMove() {

    currentMove = moves.length;

    updateBoard();
}

window.onload = function () {

    board = Chessboard("board", {
    position: "start",
    pieceTheme:
        "https://chessboardjs.com/img/chesspieces/wikipedia/{piece}.png"
});
};