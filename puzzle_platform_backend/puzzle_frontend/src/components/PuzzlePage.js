import React, { useState } from "react";
import SideNavbar from "./SideNavbar";
import Content from "./Content";
import { useLocation } from "react-router-dom";

const PuzzlePage = () => {
    const puzzles = [];
    for (let index = 0; index < 25; index++) {
        puzzles.push({ id: index + 1 });
    }

    const [selectedPuzzle, setSelectedPuzzle] = useState(null);
    const location = useLocation();
    const userEmail = location.state && location.state.email;
  

    const handleSidebarButtonClick = async (id) => {
      console.log({id, userEmail})
        try {
            const response = await fetch(
                "http://127.0.0.1:8000/api/get_ids/",
                {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify({ taskId: id, email: userEmail }),
                }
            );

            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            const data = await response.json();
            console.log(data);
            setSelectedPuzzle({ id });
        } catch (error) {
            console.error("Error sending task ID and email to backend", error);
        }
    };

    const handleDifficultyBoxButtonClick = async (id) => {
        const puzzle = Math.ceil(id / 72);
        try {
            const response = await fetch(
                "http://127.0.0.1:8000/api/handle_difficulty_box_button_click/",
                {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify({ buttonid: id }),
                }
            );

            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }

            const data = await response.json();
            console.log(data.image_path);

            setSelectedPuzzle({
                id: puzzle,
                imageUrl: data.image_path,
                videoUrl: data.video_path,
            });
            const buttons = document.querySelectorAll(".difficulty-buttons button");
            buttons.forEach((button) =>
                button.classList.remove("active-difficulty-button")
            );

            const clickedButton = document.getElementById(`button-${id}`);
            if (clickedButton) {
                clickedButton.classList.add("active-difficulty-button");
            }
        } catch (error) {
            console.error("Error fetching puzzle data", error);
        }
    };

    const renderDifficultyBoxButtons = (puzzleId, type, handleClick) => {
        const buttons = [];
        for (let i = 1; i <= 24; i++) {
            const buttonId = i + (type - 1) * 24 + (puzzleId - 1) * 72;
            buttons.push(
                <button
                    key={buttonId}
                    onClick={() => handleClick(buttonId)}
                    className={
                        selectedPuzzle?.id === buttonId ? "active active-difficulty-button" : ""
                    }
                >
                    {i}
                </button>
            );
        }
        return buttons;
    };

    return (
        <div className="puzzlepage">
            <SideNavbar
                puzzles={puzzles}
                handleSidebarButtonClick={handleSidebarButtonClick}
                selectedPuzzleId={selectedPuzzle?.id}
            />
            <Content
                selectedPuzzle={selectedPuzzle}
                renderDifficultyBoxButtons={renderDifficultyBoxButtons}
                handleDifficultyBoxButtonClick={handleDifficultyBoxButtonClick}
            />
        </div>
    );
};

export default PuzzlePage;
