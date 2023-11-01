import { useCallback, useEffect, useState } from "react";
import Box from "@mui/material/Box";
import Button from "@mui/material/Button";
import Dialog from "@mui/material/Dialog";
import DialogActions from "@mui/material/DialogActions";
import DialogContent from "@mui/material/DialogContent";
import DialogContentText from "@mui/material/DialogContentText";
import DialogTitle from "@mui/material/DialogTitle";
import { $host } from "../../utils/axios";
import { TimeBox } from "./TimeBox";
import { Backdrop, CircularProgress } from "@mui/material";

export function ReserveDialog({ open, setOpen }) {
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);
    const [reservationData, setReservationData] = useState(null);

    const [timeList, setTimeList] = useState([]);
    const [updatedTimeList, setUpdatedTimeList] = useState([]);
    const [isUpdated, setIsUpdated] = useState(false);

    const handleClose = () => {
        setOpen(null);
    };

    useEffect(() => {
        (async () => {
            if (parseInt(open)) {
                setLoading(true);

                const response = await $host.get("/meeting_room/" + open);
                if (response.status === 200) {
                    setReservationData(response.data);
                } else {
                    setError(response.message);
                }

                return setTimeout(() => setLoading(false), 500);
            } else {
                setError("The room_id must be an integer.");
            }
        })();
    }, [open]);

    useEffect(() => {
        if (!reservationData || !reservationData.time) return;
        const timeArray = new Array(56).fill(true);

        if (reservationData.time.length !== 0) {
            reservationData.time.forEach((t) => (timeArray[t] = false));
        }

        setTimeList([...timeArray]);
        setUpdatedTimeList([...timeArray]);
        return;
    }, [reservationData]);

    useEffect(() => {
        const isUpdated = updatedTimeList.some((ut, i) => ut !== timeList[i]);
        setIsUpdated(isUpdated);
    }, [updatedTimeList]);

    const { name, description, time, id } = reservationData || {};

    const handleUpdatedTime = useCallback(
        function (index, isAvailable) {
            const updatedList = [...updatedTimeList];
            updatedList[index] = isAvailable;
            setUpdatedTimeList([...updatedList]);
        },
        [updatedTimeList]
    );

    const timeArea = updatedTimeList.map((availability, index) => (
        <TimeBox
            key={"timebox" + index}
            index={index}
            defaultAvailability={timeList[index]}
            updatedAvailability={availability}
            setAvailabilityByIndex={handleUpdatedTime}
        />
    ));

    const saveReservation = useCallback(() => {
        if (!isUpdated) return;

        (async () => {
            setIsUpdated(false);

            const deleteTime = [];
            const postTime = [];
            for (let i = 0; i < timeList.length; i++) {
                if (!timeList[i] && updatedTimeList[i]) deleteTime.push(i);
                if (timeList[i] && !updatedTimeList[i]) postTime.push(i);
            }

            if (deleteTime.length) {
                const deleteResponse = await $host.delete(
                    "/meeting_room/" + open,
                    {
                        data: {
                            time: deleteTime,
                        },
                    }
                );
                if (deleteResponse.status !== 200) {
                    setError(deleteResponse.message);
                }
            }
            if (postTime.length) {
                const postResponse = await $host.post("/meeting_room/" + open, {
                    time: postTime,
                });
                if (postResponse.status !== 201) {
                    setError(postResponse.message);
                }
            }
        })();

        return setTimeout(() => {
            setIsUpdated(true);
            setOpen(null);
        }, 500);
    }, [isUpdated, updatedTimeList, timeList]);

    if (loading)
        return (
            <>
                <Dialog
                    fullWidth
                    open={Boolean(parseInt(open))}
                    onClose={handleClose}
                >
                    <DialogTitle>{name}</DialogTitle>
                    <DialogContent>
                        <Box
                            sx={{
                                width: "100%",
                                display: "flex",
                                justifyContent: "center",
                                alignContent: "center",
                            }}
                        >
                            <CircularProgress color="inherit" />
                        </Box>
                    </DialogContent>
                    <DialogActions>
                        <Button onClick={handleClose}>Close</Button>
                    </DialogActions>
                </Dialog>
            </>
        );

    return (
        <>
            <Dialog
                fullWidth
                open={Boolean(parseInt(open))}
                onClose={handleClose}
            >
                <DialogTitle>{name}</DialogTitle>
                <DialogContent>
                    <DialogContentText>{description}</DialogContentText>
                    <Box
                        sx={{
                            paddingTop: "30px",
                            display: "flex",
                            flexDirection: "column",
                            justifyContent: "center",
                            alignItems: "center",
                            gap: "20px",
                        }}
                    >
                        <Box
                            noValidate
                            component="form"
                            sx={{
                                display: "flex",
                                flexDirection: "row",
                                flexWrap: "wrap",
                                justifyContent: "center",
                                alignItems: "center",
                                m: "auto",
                                width: "fit-content",
                                gap: "6px",
                            }}
                        >
                            {timeArea}
                        </Box>
                        <Button
                            variant="outlined"
                            disabled={loading || !isUpdated}
                            sx={{
                                width: "200px",
                            }}
                            onClick={saveReservation}
                        >
                            Сохранить
                        </Button>
                    </Box>
                </DialogContent>
                <DialogActions>
                    <Button onClick={handleClose}>Close</Button>
                </DialogActions>
            </Dialog>
        </>
    );
}
