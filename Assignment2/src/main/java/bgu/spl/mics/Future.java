package bgu.spl.mics;

import java.util.concurrent.TimeUnit;
import java.util.concurrent.atomic.AtomicBoolean;

/**
 * A Future object represents a promised result - an object that will
 * eventually be resolved to hold a result of some operation. The class allows
 * Retrieving the result once it is available.
 *
 * Only private methods may be added to this class.
 * No public constructor is allowed except for the empty constructor.
 */
public class Future<T> {

	/**
	 * This should be the the only public constructor in this class.
	 */
	private T result;
	private AtomicBoolean isDone=new AtomicBoolean(false);




	public Future() {
		result = null;
	}

	/**
	 * retrieves the result the Future object holds if it has been resolved.
	 * This is a blocking method! It waits for the computation in case it has
	 * not been completed.
	 * <p>
	 * @return return the result of type T if it is available, if not wait until it is available.
	 * @pre result == null
	 * @post result != null
	 */
	synchronized public T get() {
		while(!isDone.get()){
			try{
				wait();
			}
			catch(InterruptedException e){
				return result;
			}
		}
		return result;
	}

	/**
	 * Resolves the result of this Future object.
	 * @pre this.get() == null
	 * @pre this.isDone() == false
	 * @post this.isDone() == true
	 * @post this.get() != null
	 */
	synchronized public void resolve (T result) {
		isDone.set(true);
		this.result = result;
		notifyAll();
	}
	/**
	 * @return true if this object has been resolved, false otherwise
	 */
	public boolean isDone() {
		return isDone.get();
	}

	/**
	 * retrieves the result the Future object holds if it has been resolved,
	 * This method is non-blocking, it has a limited amount of time determined
	 * by {@code timeout}
	 * <p>
	 // * @param timout 	the maximal amount of time units to wait for the result.
	 * @param unit		the {@link TimeUnit} time units to wait.
	 * @return return the result of type T if it is available, if not,
	 * 	       wait for {@code timeout} TimeUnits {@code unit}. If time has
	 *         elapsed, return null.
	 */
	public T get(long timeout, TimeUnit unit) {
		if (!isDone.get()){
			try {
				Thread.currentThread().sleep(unit.toMillis(timeout));
			}
			catch (InterruptedException e) {
				return result;
			}
		}
		return result;
	}

}