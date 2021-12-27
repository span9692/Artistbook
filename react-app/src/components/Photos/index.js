import './photos.css'

function Photos({profile_photos}) {
    return (
        <>
            <div className='photo-box'>
                <span className='photo-text'>Photos</span>
                <div className='all-photo-box'>
                    {profile_photos.map(photo => (
                        // <div>
                            <img className='all-photos' src={photo.photo}></img>
                        // </div>
                    ))}
                </div>
            </div>
        </>
    )
}

export default Photos