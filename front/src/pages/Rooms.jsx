import { Backdrop, Box, CircularProgress, Typography } from "@mui/material";

import { RoomCard } from "../components/rooms/Card";

import Room1 from "../assets/pages/meeting_rooms/1_500.jpg";
import Room2 from "../assets/pages/meeting_rooms/2_500.jpg";
import Room3 from "../assets/pages/meeting_rooms/3_500.jpg";
import Room4 from "../assets/pages/meeting_rooms/4_500.jpg";
import Room5 from "../assets/pages/meeting_rooms/5_500.jpg";
import { useEffect, useState } from "react";
import { ReserveDialog } from "../components/rooms/ReserveDialog";
import { $host } from "../utils/axios";

export function MeetingRooms() {
    const [openDialog, setOpenDialog] = useState(null);
    const dialog = {
        open: openDialog,
        setOpen: setOpenDialog,
    };

    const [roomsData, setRoomsData] = useState([]);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    useEffect(() => {
        (async () => {
            setLoading(true);

            const response = await $host.get("/meeting_room");
            if (response.status === 200) {
                setRoomsData(response.data);
            } else {
                setError(response.message);
            }

            return setTimeout(() => setLoading(false), 500);
        })();
    }, []);

    const roomsImgs = [Room1, Room2, Room3, Room4, Room5];
    const rooms = roomsData.map(({ id, name, description }, i) => (
        <RoomCard
            key={name + i}
            img={roomsImgs[i]}
            room_id={id}
            alt={name}
            title={name}
            description={description}
            setOpenDialog={setOpenDialog}
        />
    ));

    return (
        <>
            <Backdrop
                sx={{
                    color: "#fff",
                    zIndex: (theme) => theme.zIndex.drawer + 1,
                }}
                open={loading}
            >
                <CircularProgress color="inherit" />
            </Backdrop>

            <ReserveDialog {...dialog} />

            <Typography
                variant="h6"
                style={{
                    padding: "10px 10px 30px 30px",
                    textAlign: "start",
                }}
            >
                Переговорные
            </Typography>
            <Box
                sx={{
                    display: "flex",
                    flexDirection: "column",
                    gap: "20px",
                    paddingLeft: "30px",
                }}
            >
                {rooms}
            </Box>
        </>
    );
}
