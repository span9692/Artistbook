import { Link } from 'react-router-dom'
import './friendModal.css'

function AllFriends({contact_list}) {
    return (
        <>
            <div className='friend-modal-container'>
                <div className='f-text'>Friends ({contact_list.length})</div>
                <div className='f-container'>
                    {contact_list.map(friend => (
                    <Link className='link-to-friend1' to={`/users/${friend.id}`}>
                        <div key={friend.id} className='indiv-contact1'>
                            <img className='square-portraits' src={friend?.profile_pic}></img>
                            <span className='requester-name1'>{friend?.alias ? friend?.alias : friend?.first_name+' '+friend?.last_name }</span>
                        </div>
                    </Link>
                    ))}
                </div>
            </div>
        </>
    )
}

export default AllFriends